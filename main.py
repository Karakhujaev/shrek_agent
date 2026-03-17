import json

import anthropic
from anthropic.types import ToolParam
from termcolor import colored

from tools import edit_file_definition, list_files_definition, read_file_definition, search_documentation_definition


class ShrekAgent:
    def __init__(self):
        self.client = anthropic.Anthropic()
        self.tools = [
            edit_file_definition,
            read_file_definition,
            list_files_definition,
            search_documentation_definition
        ]

    def get_message(self):
        try:
            user_input = input()
            return user_input, bool(user_input)
        except EOFError as e:
            return "", str(e)

    def run(self):
        conversation = []
        print("Chat with Claude (use 'ctrl-d' to quit)")

        read_user_input = True
        while True:
            if read_user_input:
                print(colored("You: ", "blue"), end="")

                user_input, ok = self.get_message()
                if not ok:
                    break

                user_message = {
                    "role": "user",
                    "content": [{"type": "text", "text": user_input}],
                }
                conversation.append(user_message)

            message = self.run_inference(conversation)
            conversation.append({"role": "assistant", "content": message.content})

            tool_results = []
            for content in message.content:
                if content.type == "text":
                    print(colored("Claude:", "yellow"), f" {content.text}")
                elif content.type == "tool_use":
                    result = self.execute_tool(
                        content.id, content.name, json.dumps(content.input)
                    )
                    tool_results.append(result)

            if not tool_results:
                read_user_input = True
                continue

            read_user_input = False
            conversation.append({"role": "user", "content": tool_results})

    def execute_tool(self, tool_id, name, input_data):
        for tool in self.tools:
            if tool.name == name:
                print(colored("tool:", "green"), f" {name}({input_data})")
                result, error = tool.function(input_data)

                if error:
                    return {
                        "type": "tool_result",
                        "tool_use_id": tool_id,
                        "content": error,
                        "is_error": True,
                    }

                return {
                    "type": "tool_result",
                    "tool_use_id": tool_id,
                    "content": result,
                    "is_error": False,
                }

        return {
            "type": "tool_result",
            "tool_use_id": tool_id,
            "content": "tool not found",
            "is_error": True,
        }

    def run_inference(self, conversation):
        tools: list[ToolParam] = [
            {
                "name": tool.name,
                "description": tool.description,
                "input_schema": tool.input_schema,
            }
            for tool in self.tools
        ]

        return self.client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=2000,
            messages=conversation,
            tools=tools,
        )


def main():
    shreg_agent = ShrekAgent()
    shreg_agent.run()


if __name__ == "__main__":
    main()

# Best Practices

## Code Quality

### Write Clear, Self-Documenting Code
- Use descriptive variable and function names
- Keep functions small and focused (single responsibility)
- Avoid deep nesting; prefer early returns

```python
# Prefer this
def process_order(order):
    if not order.is_valid():
        return None
    if not order.has_items():
        return None
    return calculate_total(order)

# Over this
def process_order(order):
    if order.is_valid():
        if order.has_items():
            return calculate_total(order)
    return None
```

### Error Handling
- Catch specific exceptions, not generic ones
- Provide meaningful error messages
- Log errors with context for debugging
- Fail fast on unrecoverable errors

### Testing
- Write tests before or alongside code
- Test behavior, not implementation details
- Use descriptive test names that explain the scenario
- Keep tests independent and isolated

## Security

### Input Validation
- Validate all user input on the server side
- Use parameterized queries for database operations
- Sanitize output to prevent XSS

### Secrets Management
- Never commit secrets to version control
- Use environment variables or secret managers
- Rotate credentials regularly

### Authentication
- Use established libraries, don't roll your own crypto
- Implement proper session management
- Use HTTPS everywhere

## Performance

### Database
- Index frequently queried columns
- Avoid N+1 query problems
- Use connection pooling

### Caching
- Cache expensive computations
- Set appropriate TTLs
- Invalidate cache when data changes

### Async Operations
- Use async for I/O-bound operations
- Don't block the event loop
- Implement timeouts for external calls

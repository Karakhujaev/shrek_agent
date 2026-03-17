# API Reference

## Authentication

All API requests require authentication via Bearer token in the Authorization header.

```
Authorization: Bearer <your-api-key>
```

## Base URL

```
https://api.example.com/v1
```

## Endpoints

### Users

#### GET /users
Retrieve a list of users.

**Query Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| limit | integer | 20 | Max results per page (1-100) |
| offset | integer | 0 | Number of results to skip |
| status | string | all | Filter by status: active, inactive, all |

**Response:**
```json
{
  "data": [
    {"id": "usr_123", "email": "user@example.com", "status": "active"}
  ],
  "meta": {"total": 100, "limit": 20, "offset": 0}
}
```

#### POST /users
Create a new user.

**Request Body:**
```json
{
  "email": "newuser@example.com",
  "name": "John Doe",
  "role": "member"
}
```

#### GET /users/:id
Retrieve a specific user by ID.

#### PATCH /users/:id
Update user properties.

#### DELETE /users/:id
Delete a user (soft delete).

### Resources

#### GET /resources
List all resources with pagination.

#### POST /resources
Create a new resource.

#### GET /resources/:id
Get resource details.

## Error Responses

```json
{
  "error": {
    "code": "validation_error",
    "message": "Invalid email format",
    "field": "email"
  }
}
```

## Rate Limits

- 1000 requests per minute per API key
- 429 status code when exceeded

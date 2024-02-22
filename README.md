# Semanticometer API
The Model API allows users to query various natural language processing models to analyze sentiment and objectivity of text inputs. The API supports both single and bulk queries.

## API Usage

This section details how to interact with the Model API endpoints to perform sentiment and objectivity analysis on text inputs.

### Single Query

To perform a sentiment or objectivity analysis on a single text input, make a POST request to the `/api/single` endpoint with the following parameters:

- **URL:** `/api/single`
- **Method:** `POST`
- **Query Parameters:**
  - `model`: The name of the model to be used for analysis. Choose from 'vs' (Vader Sentiment), 'tbp' (TextBlob Polarity), 'tbo' (TextBlob Objectivity), 'pr' (Perspective).
- **Request Body:**
  - `sentence`: The text input to be analyzed.

#### Example

```http
POST /api/single?model=vs HTTP/1.1
Content-Type: application/json

{
    "sentence": "This is a sample text for sentiment analysis."
}
```

### Bulk Query

To perform sentiment or objectivity analysis on multiple text inputs in bulk, make a POST request to the `/api/bulk` endpoint with the following parameters:

- **URL:** `/api/bulk`
- **Method:** `POST`
- **Request Body:**
  - `sentences`: A list of text inputs to be analyzed in bulk.

#### Example

```http
POST /api/bulk HTTP/1.1
Content-Type: application/json

{
    "sentences": [
        "This is sentence 1.",
        "This is sentence 2.",
        "This is sentence 3."
    ]
}
```

### Response

Upon successful execution of the requests, the API will return a JSON response containing the analysis results:

- `results`: The analysis results returned by the specified model(s) for the provided text input(s).

### Error Handling

If there are any issues with the request parameters or the specified model is not supported, the API will return a `400 Bad Request` response with an error message.

# Import the re module for regular expressions
# Flask app configuration
# Enable CORS for all routes
# Configure the upload directory
# Create the upload directory if it doesn't exist
# Initialize EasyOCR for English language
# Ensure the API key is stored in an environment variable
# Replace with your key
# Get the API key from the environment variable
# Format extracted text into structured paragraphs or bullet points.
# Split text into paragraphs based on double newlines or sentence boundaries
# Create bullet points from paragraphs
# Extract text from PDF files and format it into structured content.
# Split text into sentences using regular expressions
# Extract text from audio files and format it into structured content.
# Extract text from images and format it into structured content.
# Use EasyOCR to read text from image
# Extract keywords using the Gemini API.
# Start a chat session and send the input text
# Start a new Gemini chat session
# Send text to Gemini for processing
# Split the response by lines to extract keywords
# Extract keywords from Gemini response
# Matches "Heading:" format # Regex to find potential side headings
# Select only the first 10 keywords
# Select first 10 keywords
# Print the API error
# Generate a tree-structured knowledge graph from keywords, limiting each node to two words.
# Use a directed graph for tree structure
# Create a root node
# Function to limit each keyword to two words
# Take the first two words
# Add keywords as children of the root node
# Limit keyword to two words
# Add limited keyword to graph
# Connect limited keyword to the root node
# Layout for a better visual representation
# Draw graph using Matplotlib
# Path to save the knowledge graph image
# Return the name of the saved knowledge graph file
# Serve uploaded files.
# Serve uploaded files from the uploads folder
# Get the uploaded file
# Secure the filename for safe saving
# Construct the file path
# Save the uploaded file
# Determine file type and extract text
# Extract keywords and generate knowledge graph
# Join structured text for keywords
# Generate knowledge graph if keywords are found
# Will be a list of bullet points now
# Return error message as JSON response
# Render the upload template for GET requests
# Run the Flask application in debug mode
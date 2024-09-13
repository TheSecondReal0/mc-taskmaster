# Stage 1: Install dependencies and build
FROM node:18.19.1-alpine AS builder

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json before copying other files
COPY app/package*.json ./

# Remove node_modules and package-lock.json (npm bug fix)
RUN rm -rf node_modules package-lock.json

# Install dependencies
RUN npm install

# Copy the rest of the project files
COPY app/ .

# Build the project
RUN npm run build



# Stage 2: Production environment
FROM node:18.19.1-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the built files from the previous stage
COPY --from=builder /app /app

# Install only production dependencies
RUN npm install --omit=dev

# Expose the application port
EXPOSE 3000

# Command to run the app
CMD ["npm", "run", "start"]

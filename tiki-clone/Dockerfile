FROM node:16.15-alpine

# Install Yarn
RUN apk add --no-cache yarn

# Set the working directory
WORKDIR /app

# Copy package.json and yarn.lock to the container
COPY package*.json yarn.lock ./

# Install dependencies
RUN yarn install

# Copy the rest of the application files to the container
COPY . .

# Expose port 5173
EXPOSE 5173

# Start the application
CMD ["yarn", "dev", "--", "--host", "0.0.0.0"]

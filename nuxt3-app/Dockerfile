FROM node:16.10.0-alpine

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
RUN apk update && apk upgrade && apk add git

ADD . /usr/src/app/
RUN npm install

# Build app
RUN npm run build

ENV HOST 0.0.0.0
EXPOSE 3000

# start command
CMD [ "npm", "run", "start" ]

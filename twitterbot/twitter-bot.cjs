const {TwitterApi} = require("twitter-api-v2");

const client = new TwitterApi({
    appKey: "VbTFobZst0d0rgS1HzpZZaLKp",
    appSecret: "GXtyPKL2IA7bLlpE3cn9zhx2LsCCTzkXr6kOrkIBYjoPrN4i5s",
    accessToken: "1503737831826636800-0A0xkNnXXHlwgZAvzNvCegjLn4QZNb",
    accessSecret: "RwJdd3IdjUjMtclVyJVIFDcuinEG86KgbrpkXN4aNv1bQ",
})

const rwClient = client.readWrite

module.exports = rwClient
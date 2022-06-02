const {TwitterAPI} = require("twitter-api-v2");

const client = new TwitterAPI({
    appKey: "Ivzo5OtlPHH8tPE9WQoe49YBK",
    appSecret: "4ej3WuPaqIb7OpqGBpJnyYUu5ILigZGtd2tnm7SyOwi27quhPV",
    accessToken: "2369370654-nSrSVPvUKY6A3YFqMYQiiKSCmwwBHX28i6wtMNe",
    accessSecret: "mqyhlo4oiyZZan5rKnpbq3paXHa3ZxmwDjqTvnMXQvK9I",
})

const rwClient = client.readWrite

module.exports = rwClient
const rwClient = require("./twitter-bot.cjs");

const tweet = async () => {
    try {
        await rwClient.v1.tweet("Is this working?")
    } catch (e){
        console.error(e)
    }
}

tweet()
const path = require("path");

const root = path.join(__dirname, "./../");
const src = path.join(root, "./src/");
const build = path.join(root, "./build/");

module.exports = {

    paths: {
        root,
        src,
        build,
    },

};

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

    serve: {
        server: {
            baseDir: build,
        },

        port: 3000,
    },

    templates: {
        path: src + "templates/",
        beautifyHtml: true,
    },

    styles: {
        path: src + "styles/",
    },

    scripts: {
        path: src + "scripts/",
    },

    images: {
        path: src + "images/",
    },

};

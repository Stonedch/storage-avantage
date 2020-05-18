const gulp = require("gulp");
const pug = require("gulp-pug");

const config = require("../../config");

function buildTemplates(done) {
    gulp.src(config.templates.path + "*.pug")
        .pipe(pug({pretty: config.templates.beautifyHtml}))
        .pipe(gulp.dest(config.paths.build));

    done();
}

gulp.task("build:templates", buildTemplates);

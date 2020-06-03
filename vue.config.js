let WebpackChain = import('webpack-chain')

module.exports = {
    publicPath: './',
    // build output dir
    outputDir: 'dist',
    // Set the output dir for static resources.
    assetsDir: 'static',
    // Disable source map.
    productionSourceMap: false,
    // Disable filename hash
    filenameHashing: true,

    /**
     * Typescript in Webpack
     *
     * @param {WebpackChain} config
     */
    chainWebpack: (config) => {
        config
            .resolve
            .extensions
            .add('.ts')
            .add('.tsx')
            .end()
            .end()
            .module
            .rule('typescript')
            .test(/\.tsx?$/)
            .use('babel-loader')
            .loader('babel-loader')
            .end()
            .use('ts-loader')
            .loader('ts-loader')
            .options({
                transpileOnly: true,
                appendTsSuffixTo: [
                    '\\.vue$',
                ],
                happyPackMode: false
            })
            .end()
    }
}

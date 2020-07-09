<template>
    <div id="youtube-player" class="col embed-responsive embed-responsive-16by9">
        <iframe class="embed-responsive-item"
                :src="standardize(src)"
                allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen></iframe>
    </div>
</template>

<script>
    export default {
        name: "YoutubePlayer",
        props: {
            src: String
        },
        methods: {
            standardize (src) {
                if (src) {
                    if (src.indexOf("&autoplay=1") < 0) {
                        return `${src}&autoplay=1`
                    }
                }
            }
        }
    }
</script>

<style scoped>

</style>

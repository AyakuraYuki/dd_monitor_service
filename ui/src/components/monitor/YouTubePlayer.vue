<template>
    <div id="youtube-player" class="col embed-responsive embed-responsive-16by9">
        <iframe class="embed-responsive-item"
                :src="src"
                allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen></iframe>
    </div>
</template>

<script>
    export default {
        name: "YoutubePlayer",
        props: {
            src: String
        }
    }
</script>

<style scoped>

</style>

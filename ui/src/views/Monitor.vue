<template>
    <div id="monitor" class="monitor container-fluid">
        <div class="row" v-for="(row, index) in playlist" :key="index">
            <youtube-player :src="link" v-for="(link, innerIndex) in row" :key="innerIndex"/>
        </div>
    </div>
</template>

<script>
    import { playlist } from "../api/player"
    import YoutubePlayer from "../components/monitor/YouTubePlayer"

    export default {
        name: "Monitor",
        components: {
            YoutubePlayer
        },
        data() {
            return {
                playlist: []
            }
        },
        methods: {
            // 获取播放列表
            fetchPlaylist() {
                playlist().then(res => {
                    let data = res.data
                    this.playlist = data.playlist
                })
            }
        },
        mounted() {
            this.fetchPlaylist()
            document.body.classList.add('bg-dark')
        }
    }
</script>

<style scoped>

</style>

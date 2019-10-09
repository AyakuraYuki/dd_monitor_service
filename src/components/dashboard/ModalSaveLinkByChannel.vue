<template>
    <b-modal centered id="add-channel" title="Add Channel" size="lg"
             @ok="save" ok-title="Save" cancel-title="Cancel" @cancel="cleanup" @close="cleanup">
        <form ref="saveByChannelForm">
            <b-form-group label-for="title-input">
                <b-input-group prepend="Title" class="mt-3">
                    <b-form-input id="title-input" v-model="post.title"
                                  placeholder="Title or description of Stream"></b-form-input>
                </b-input-group>
            </b-form-group>
            <b-form-group label-for="channel-input">
                <b-input-group prepend="YouTube Channel Id" class="mt-3">
                    <b-form-input id="channel-input" v-model="post.channel"
                                  placeholder="For example: UC-hM6YJuNYVAmUWxeIr9FeA (also support full channel link)"></b-form-input>
                </b-input-group>
            </b-form-group>
        </form>
    </b-modal>
</template>

<script>
    import { saveLinkByChannel } from "../../api/dashboard"

    export default {
        name: "ModalSaveLinkByChannel",
        data() {
            return {
                post: {
                    title: '',
                    channel: ''
                }
            }
        },
        methods: {
            save() {
                saveLinkByChannel(this.post).then(() => {
                    this.cleanup()
                    this.$emit('update:linkList')
                })
            },
            cleanup() {
                this.post.title = ''
                this.post.channel = ''
            }
        }
    }
</script>

<style scoped>

</style>

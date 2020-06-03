<template>
    <b-modal centered id="edit-link" :title="modalTitle()" size="lg"
             @ok="save" ok-title="Save" cancel-title="Cancel">
        <form ref="saveForm">
            <b-form-input v-model="link._id" v-if="link._id" v-show="false"/>
            <b-form-group label-for="title-input">
                <b-input-group prepend="Title" class="mt-3">
                    <b-form-input id="title-input" v-model="link.title"></b-form-input>
                </b-input-group>
            </b-form-group>
            <b-form-group label-for="link-input">
                <b-input-group prepend="Link" class="mt-3">
                    <b-form-input id="link-input" v-model="link.link"></b-form-input>
                </b-input-group>
            </b-form-group>
            <b-form-group label-for="sort-input" v-if="link._id">
                <b-input-group prepend="Sort" class="mt-3">
                    <b-form-input id="sort-input" type="number" v-model="link.sort"></b-form-input>
                </b-input-group>
            </b-form-group>
        </form>
    </b-modal>
</template>

<script>
    import { saveLink, updateLink } from "../../api/dashboard"
    import { REQUEST_POST, REQUEST_PUT } from "../../api/api"

    export default {
        name: "ModalEditLink",
        props: {
            method: String,
            item: {}
        },
        data () {
            return {
                link: {}
            }
        },
        watch: {
            item (val) {
                this.handleLink(val)
            }
        },
        methods: {
            handleLink (val) {
                this.link = {
                    _id: val && val._id ? val._id : 0,
                    title: val && val.title ? val.title : '',
                    link: val && val.link ? val.link : '',
                    sort: val && val.sort ? val.sort : 1
                }
            },
            save () {
                if (this.method) {
                    if (this.method === REQUEST_POST) {
                        saveLink(this.link).then(() => {
                            this.$emit('update:linkList')
                        })
                    } else if (this.method === REQUEST_PUT) {
                        updateLink(this.link._id, this.link).then(() => {
                            this.$emit('update:linkList')
                        })
                    }
                }
            },
            // cancel() {
            //     this.method = ''
            //     this.item = undefined
            // },
            modalTitle () {
                if (this.item && this.item._id) {
                    return 'Edit stream'
                }
                return 'Add stream'
            }
        }
    }
</script>

<style scoped>

</style>

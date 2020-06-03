<template>
    <b-modal id="edit-link-v2"
             :title="getTitle()"
             :visible.sync="visible"
             size="lg"
             @ok="handleAdd"
             ok-title="Save"
             @cancel="handleClose"
             cancel-title="Cancel"
             centered>
        <form ref="saveForm">
            <b-form-input v-model="link._id" v-if="link._id" v-show="false"/>

            <b-form-group label-for="title-input">
                <b-input-group prepend="Title" class="mt-3">
                    <b-form-input id="title-input" v-model="link.title"/>
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

    export default {
        name: "EditLink",
        props: {
            show: {
                type: Boolean,
                default: false
            },
            edit: {
                type: Object,
                default: null
            }
        },
        watch: {
            show (val) {
                this.visible = val
            },
            edit (val) {
                this.handleResetEdit(val)
            }
        },
        data () {
            return {
                visible: this.show,
                link: {
                    _id: 0,
                    title: undefined,
                    link: undefined,
                    sort: 9999
                }
            }
        },
        methods: {
            getTitle () {
                if (this.edit) {
                    return 'Edit Stream'
                }
                return 'Add Stream'
            },
            handleResetEdit (val) {
                if (val) {
                    Object.assign(this.link, val)
                } else {
                    this.link = {
                        _id: 0,
                        title: '',
                        link: '',
                        sort: 9999
                    }
                }
            },
            handleClose () {
                this.handleResetEdit()
                this.$emit('close')
            },
            handleRestForm () {
                this.handleClose()
                this.$nextTick(() => {
                    this.handleResetEdit()
                }, 200)
                this.$emit('success')
            },
            handleAdd () {
                if (this.edit) {
                    updateLink(this.link._id, this.link).then(() => {
                        this.handleRestForm()
                    })
                } else {
                    saveLink(this.link).then(() => {
                        this.handleRestForm()
                    })
                }
            }
        }
    }
</script>

<style scoped>

</style>

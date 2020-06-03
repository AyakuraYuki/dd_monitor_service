export default {
    data () {
        return {
            editDetail$: {
                show: false,
                edit: null
            }
        }
    },
    methods: {
        $_edit_handleCloseDialog () {
            this.editDetail$.edit = null
            this.editDetail$.show = false
        },
        $_edit_handleShowDialog (edit) {
            this.editDetail$.edit = edit
            this.editDetail$.show = true
        },
        $_edit_handleShowDialogForCopy (edit) {
            edit.id = ''
            this.editDetail$.edit = edit
            this.editDetail$.show = true
        }
    }
}

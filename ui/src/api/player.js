import api from './api'

export const playlist = () => {
    const uri = '/player/list'
    return api.get(uri)
}

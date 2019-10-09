import api from './api'

// region Link

export const linkList = ({ query }) => {
    const uri = '/_/link'
    const params = {}
    if (query !== '') {
        params.query = query
    }
    return api.get(uri, {
        params: params
    })
}

export const saveLink = ({ title, link }) => {
    const uri = '/_/link'
    return api.post(uri, { title, link })
}

export const saveLinkByChannel = ({ title, channel }) => {
    const uri = '/_/link/save/channel'
    return api.post(uri, { title, channel })
}

export const getLink = (linkId) => {
    const uri = `/_/link/lid/${linkId}`
    return api.get(uri)
}

export const updateLink = (linkId, { title, link, sort }) => {
    const uri = `/_/link/lid/${linkId}`
    return api.put(uri, { title, link, sort })
}

export const deleteLink = (linkId) => {
    const uri = `/_/link/lid/${linkId}`
    return api.delete(uri)
}

// endregion

// region Channel

export const channelList = (query) => {
    const uri = '/_/channel'
    const params = {}
    if (query) {
        params.query = query
    }
    return api.get(uri, {
        params: params
    })
}

export const saveChannel = ({ name, channelId }) => {
    const uri = '/_/channel'
    return api.post(uri, { name, channelId })
}

export const getChannel = (cid) => {
    const uri = `/_/channel/cid/${cid}`
    return api.get(uri)
}

export const updateChannel = (cid, { name, channelId }) => {
    const uri = `/_/channel/cid/${cid}`
    return api.put(uri, { name, channelId })
}

export const deleteChannel = (cid) => {
    const uri = `/_/channel/cid/${cid}`
    return api.delete(uri)
}

// endregion

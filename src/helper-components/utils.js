export const randomID = () => Math.random().toString().substr(2);

function CustomEvent(event, params) {
    // eslint-disable-next-line no-param-reassign
    params = params || {
        bubbles: false,
        cancelable: false,
        // eslint-disable-next-line no-undefined
        detail: undefined,
    };
    const evt = document.createEvent('CustomEvent');
    evt.initCustomEvent(
        event,
        params.bubbles,
        params.cancelable,
        params.detail
    );
    return evt;
}

export const isInternalLink = (href) => href.startsWith('/');

export const updateLocation = (e, href) => {
    if (!isInternalLink(href)) {
        return;
    }
    e.preventDefault();
    window.history.pushState({}, '', href);
    window.dispatchEvent(new CustomEvent('_dashprivate_pushstate'));
    window.scrollTo(0, 0);
};

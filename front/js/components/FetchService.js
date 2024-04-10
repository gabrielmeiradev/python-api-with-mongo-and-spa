class FetchService {
    constructor(apiBaseUrl) {
        this.apiBaseUrl = apiBaseUrl;
    }

    async fetch(url, options = {}) {
        let newUrl = `${this.apiBaseUrl}${url}`;
        const response = await fetch(newUrl, options);
        console.log(newUrl)
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    }
}
export default FetchService;
export function get_token() {
    const token = localStorage.getItem('token');
    const expiredTime = localStorage.getItem('expiredTime');
    if (Date.now() < expiredTime){
        const lifeTime = localStorage.getItem('lifetime');
        localStorage.setItem('expiredTime', Date.now() + lifeTime * 1000);
        return token;
    };
    return null;
};

export function check_is_auth() {
    const token = localStorage.getItem('token');
    const expiredTime = localStorage.getItem('expiredTime');
    return Date.now() < expiredTime && Boolean(token);
}

export function get_bearer() {
    return check_is_auth() ? `Bearer ${get_token()}` : null
}

export function throw_body(body) {
    for (const [key, value] of Object.entries(body)) {
        value.forEach(function (item, index) {
            console.log(`${key} - ${item}`);
        });
    }
}

export async function parse_response(response) {
    return {
        status: response.status,
        body: await response.json().catch(_ => {})
    };
}
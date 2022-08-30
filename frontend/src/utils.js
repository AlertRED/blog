export function get_token() {
    const storage = localStorage;
    const token = storage.getItem('token');
    const expiredTime = storage.getItem('expiredTime');
    if (Date.now() < expiredTime){
        const lifeTime = storage.getItem('lifetime');
        storage.setItem('expiredTime', Date.now() + lifeTime * 1000);
        return token;
    };
    return null;
};

export function is_auth() {
    const storage = localStorage;
    const token = storage.getItem('token');
    const expiredTime = storage.getItem('expiredTime');
    if (Date.now() < expiredTime && token){
        return true;
    };
    return false;
}

export function get_bearer() {
    return is_auth() ? `Bearer ${get_token()}` : null
}
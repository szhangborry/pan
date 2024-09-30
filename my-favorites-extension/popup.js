const urlInput = document.getElementById('url');
const addButton = document.getElementById('addButton');
const favoritesList = document.getElementById('favoritesList');

addButton.addEventListener('click', () => {
    const url = urlInput.value.trim(); // 去除前后的空格
    if (url) {
        // 验证URL是否可用
        checkUrlAvailability(url).then(isAvailable => {
            if (isAvailable) {
                chrome.storage.sync.get(['favorites'], (result) => {
                    const favorites = result.favorites || [];
                    favorites.push(url);
                    chrome.storage.sync.set({ favorites }, () => {
                        urlInput.value = '';
                        displayFavorites();
                    });
                });
            } else {
                alert('无法访问该网址，请检查输入的URL.');
            }
        }).catch(err => {
            alert('发生错误：' + err);
        });
    } else {
        alert('请输入有效的网址。');
    }
});

function checkUrlAvailability(url) {
    return fetch(url, { method: 'HEAD' }) // 使用HEAD请求只获取响应头
        .then(response => {
            return response.ok; // 如果响应状态为200-299，返回true
        })
        .catch(() => {
            return false; // 如果请求失败，则返回false
        });
}

function displayFavorites() {
    chrome.storage.sync.get(['favorites'], (result) => {
        favoritesList.innerHTML = '';
        const favorites = result.favorites || [];
        favorites.forEach((favorite, index) => {
            const li = document.createElement('li');
            li.textContent = favorite;

            const deleteButton = document.createElement('button');
            deleteButton.textContent = '删除';
            deleteButton.addEventListener('click', () => {
                favorites.splice(index, 1); // 删除对应的收藏
                chrome.storage.sync.set({ favorites }, displayFavorites); // 更新存储并重新显示
            });

            li.appendChild(deleteButton); // 将删除按钮添加到列表项中
            favoritesList.appendChild(li);
        });
    });
}

displayFavorites();

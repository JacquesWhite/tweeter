function focusElem(elem) {
    elem.style.boxShadow = "none"
    elem.style.top = "0px"
}

function blurElem(elem) {
    elem.style.boxShadow = "-20px 0 40px 0 rgba(0,0,0,0.3)"
    elem.style.top = "2px"
}

function hideResults(results) {
    for (let i = 0; i < results.length; i++) {
        results.item(i).style.display = "none"
    }
}


window.onload = function () {

    function filterUsers(e) {
        const filter = e.target.value.toUpperCase()

        for (let i = 0; i < users.length; i++) {
            let username = users.item(i).getElementsByTagName("a").item(0).innerText.toUpperCase()
            if (username) {
                if (username.indexOf(filter) > -1) {
                    users.item(i).style.display = "block"
                } else {
                    users.item(i).style.display = "none"
                }
            }
        }
    }

    const users = document.getElementsByClassName('user')
    const searcher = document.getElementsByTagName("aside").item(0)
    const input = document.getElementById('user-input')
    for (let i = 0; i < users.length; i++) {
        users.item(i).addEventListener('click', () => {
            location.href = window.location + users.item(i).id + '/'
        })
        users.item(i).addEventListener('mouseenter', () => {
            users.item(i).style.backgroundColor = '#4272d7'
        })
        users.item(i).addEventListener('mouseleave', () => {
            users.item(i).style.backgroundColor = 'white'
        })
    }


    input.onfocus = () => {
        focusElem(searcher)
    }
    input.onblur = () => {
        setTimeout(() => {
            blurElem(searcher)
            hideResults(users)
        }, 200)

    }
    input.addEventListener('input', filterUsers)

    console.log('[SEARCH] engine loaded.')


}


window.onload = async function loadPost(){
    posts = await getPosts()
    console.log(posts)
    const post_list = document.getElementById("posts")

    posts.forEach(post => {

        const newPost = document.createElement("div");
        newPost.setAttribute("id",post.id)
        newPost.innerText = post.title
        newPost.setAttribute("onclick","postDetail(this.id)")
        post_list.appendChild(newPost)
    });
}

function postDetail(e){

    var detail_link = location.href+e
    console.log(detail_link)
    location.href=detail_link

} 

window.onload = async function loadPost(){
    post_one = await getPost()
    console.log(post_one)
    const post_list = document.getElementById("post")

    const newPost = document.createElement("div");
    newPost.setAttribute("id",post.id)
    newPost.innerText = post.title
    post_list.appendChild(newPost)

}


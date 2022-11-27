
const backend_base_url = "http://127.0.0.1:8000/"
const frontend_base_url = "http://127.0.0.1:8000/front/"



async function createPost(){
    const title = document.getElementById("postTitle").value
    console.log(title)
    const email = document.getElementById("postEmail").value
    const content = document.getElementById("postContent").value
    const formdata = new FormData();

    formdata.append('title',title)
    formdata.append('content',content)
    formdata.append('email',email)

    const response = await fetch(`${backend_base_url}post/post/`,{

        method:'POST',
        body:formdata
    }
    )

    if (response.status==200){
        window.location.replace(`${frontend_base_url}/`);

    }else{
        alert(response.status)
    }



}


async function getPosts(){
    const response = await fetch(`${backend_base_url}post/post/`,{
        method:"GET",
    }
    )

    response_json = await response.json()
    return response_json
}

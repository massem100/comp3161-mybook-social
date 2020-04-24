<template>

    <nav class="navbar navbar-expand navbar-dark bg-transparent text-black fixed-top">
        <a class="navbar-brand text-black" href="#"> <img class = "header-img " src = '/static/uploads/mybook.jpg'>  MyBook</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class = "navbar-nav mr-auto">

                </ul>
            
            <ul class="navbar-nav" >

                <li class="nav-item ">
                    <router-link class="nav-link d-flex justify-content-end text-black" to="/login"> Login <span class="sr-only">(current)</span></router-link>
                </li>
                <li class="nav-item ">
                    <router-link class="nav-link d-flex justify-content-end text-black" to="/signup">Sign Up <span class="sr-only">(current)</span></router-link>
                </li>
        </ul>
        </div>
        </nav>
    
</template>

<script>
export default {
    name: 'app_header', 
    data: '', 
    components: {

    }
    
}
</script>
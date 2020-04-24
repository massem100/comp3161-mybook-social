<template>
    
    <div> 
    <app-header> </app-header>
    <div class = "d-flex flex-row">
    

    <div class = "d-flex flex-column justify-content-center col-md-5 ml-4 bg-light rounded border p-4 shadow">
        <div class = "wrap-login100  d-flex flex-column align-self-center">
            <div class = "mb-5">
                <h2 class = "text-center font-weight-bold"> Welcome to MyBook </h2>
                
            </div>

            <div>
                <form class = "form-group ml-4">
                    <div class="form-group ">
                        <label for="exampleInputEmail1">Email address</label>
                        <input type="email" class="form-control " placeholder = "johndoe@example.com">
                        <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
                    </div>
                    <div class="form-group">
                        <label for="exampleInputPassword1">Password</label>
                        <input type="password" class="form-control " id="exampleInputPassword1">
                    </div>
                   
                    <div class = "d-flex justify-content-center">
                        <button type="submit" class="btn btn-theme w-75 text-white font-weight-bold" @click = "ShowDashboard">Login</button>
                    </div>


                    <div class="text-center p-t-115 mt-4">
						<span class="txt1">
							Don’t have an account?
						</span>

                        <router-link to='/signup'>Sign Up</router-link>

                        <div> 

                        <router-link to= '/dashboard' > Press me to get to the dash</router-link>
                        </div> 
                        
					</div>
                </form>
            </div>
        </div> 
       
    </div>
    
    <img src = "/static/uploads/convo.png" class = "home-image">
    
    </div>
        
        </div>
    
</template>

<script>
import appheader  from 'components/app-header.vue'

export default {
    name: 'login_page', 
    data: '', 
    components:{

    }
}
</script>
<template>
  <div>
    <div> 
    <!-- Handles the Sign Up Form -->
    
    <app-header> </app-header>
    <div>
     
        <div class = "d-flex flex-column justify-content-center col-lg-6 bg-light rounded border p-3 shadow h-50">
                        
    <div class="">

        <div class=" o-hidden border-0 shadow-lg my-5">
        <div class="card-body p-0">
            
            <div class="row">
            <div class="">

                <div class="p-5">
                    <div class="text-center mb-4">
                        <h4 class=" text-gray font-weight-bold mb-5">Create an Account!</h4>
                    </div>

                <form class="user">
                    <div class="form-group row">
                        <div class="col-sm-6 mb-3 mb-sm-0">
                            <input type="text" class="form-control form-control-user" id="exampleFirstName" placeholder="First Name">
                        </div>

                    <div class="col-sm-6">
                        <input type="text" class="form-control form-control-user" id="exampleLastName" placeholder="Last Name">
                    </div>

                    </div>
                    <div class="form-group">
                    <input type="email" class="form-control form-control-user" id="exampleInputEmail" placeholder="Email Address">
                    </div>
                    <div class="form-group row">
                    <div class="col-sm-6 mb-3 mb-sm-0">
                        <input type="password" class="form-control form-control-user" id="exampleInputPassword" placeholder="Password">
                    </div>
                    <div class="col-sm-6">
                        <input type="password" class="form-control form-control-user" id="exampleRepeatPassword" placeholder="Repeat Password">
                    </div>
                    </div>
                    <a href="login.html" class="btn btn-theme text-white btn-block">
                    Register Account
                    </a>
                </form>
                <hr>
                <div class="text-center">
                    <a class="small" href="login.html">Already have an account? Login!</a>
                </div>
                </div>
            </div>
            </div>
        </div>
        </div>

    </div>
                </div>
            </div> 
        </div>

        <img src = "/static/uploads/convo.png" class = "home-image">

        </div>
    
</template>

<script>
export default {
    name: 'signup_page', 
    components: {

    }

}
</script>

<style>

</style>
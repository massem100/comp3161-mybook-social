'use strict';
window.onload = ()=> {

    $('#settings').addEventListener




<<<<<<< HEAD
};
=======

        }
    },

    methods: {

    }
});

Vue.component('app-footer', {
    template: `
    <footer>
        <div class="container">
            <p>Copyright &copy; Flask Inc.</p>
        </div>
    </footer>
    `
});

Vue.component('dash-header', {
    template: `
    <nav class="navbar navbar-expand navbar-dark bg-theme text-white fixed-top">
      <a class="navbar-brand text-white" href="#">  MyBook</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
    
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
             <ul class = "navbar-nav mr-auto">

             </ul>
        
        <ul class="navbar-nav" >
            <li class="nav-item ">
                
                
            <router-link class="nav-link d-flex justify-content-end text-white" to="/logout"> My Account <span class="sr-only">(current)</span>
          
            </router-link>

                       
            <li class="nav-item ">
                <router-link class="nav-link d-flex justify-content-end text-white" to="/logout"> Logout <span class="sr-only">(current)</span></router-link>
            </li>
            <div>
  
            
       </ul>
      </div>
    </nav>
    
    
    
    `

});



const NotFound = Vue.component('not-found', {
    template: `
    <div>
        <h1>404 - Not Found</h1>
    </div>
    `,
    data: function () {
        return {}
    }
});

const Login = Vue.component('login-page', {
    template: `
    
    <div> 
    <app-header> </app-header>
    <div class = "d-flex flex-row">
    

    <div class = "enable-shadows d-flex flex-column justify-content-center col-md-5 ml-4 bg-light rounded border p-4 shadow-lg">
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
    
`,
    data: function () {

        return {

        }
    },

    methods: {
        ShowDashboard: function () {

        },


    }
});

const SignUp = Vue.component('sign-up', {
    template:

        `
    
     <div> 
    <app-header> </app-header>
    <div class = "d-flex flex-row">
    

    <div class = "enable-shadows d-flex flex-column justify-content-center col-md-5 ml-4 bg-light rounded border p-4 shadow-lg">
        <div class = "wrap-login100  d-flex flex-column align-self-center">
            <div class = "mb-5">
                <h2 class = "text-center font-weight-bold"> Welcome to MyBook </h2>
                
            </div>

            <div>
                <form class = "form-group ml-4">
                <div>
                    <h6 class = "text-center ">
                    It's quick and easy! Enter your info to get an account!
                    </h6>
                </div>
                    <div class="form-group ">
                        <label for="f_name">First Name</label>
                        <input id = "f_name"type="text" class="form-control " placeholder = "Jane">
                        
                    </div>
                    <div>
                    
                       <label for="l_name">Last Name</label>
                        <input type="text" class="form-control " id="l_name">
                    </div>
                    <div class="form-group">
                        <label for="account_email">Email </label>
                        <input type="email" class="form-control " id="account_email">
                    </div>

                     <div class="form-group">
                        <label for="l_name">Gender</label>
                        <select id="gender" name="gender">
                            <option value="" disabled>Select Gender</option>
                            <option value="Male">Male</option>
                            <option value="Female">Female</option>
                           
                        </select>
                    </div>
                     <div class="form-group">
                        <label for="l_name">Last Name</label>
                        <input type="text" class="form-control " id="l_name">
                    </div>
                     <div class="form-group">
                        <label for="dob">Date of Birth</label>
                        <input type="date"class="form-control " id="dob">
                    </div>
                   
                    <div class = "d-flex justify-content-center">
                        <button type="submit" class="btn btn-theme w-75 text-white font-weight-bold" > Sign Up</button>
                    </div>


                    <div class="text-center p-t-115 mt-4">
						<span class="txt1">
							Don’t have an account?
						</span>

                        <router-link to='/signup'>Sign Up</router-link>

                        <div> 

                       
                        </div> 
                        
					</div>
                </form>
            </div>
        </div> 
       
    </div>
    
    <img src = "/static/uploads/convo.png" class = "home-image">
    
    </div>
        
        </div>
    
    `

});

Vue.component('card', {
    template: 
    `
    <div class="card gedf-card">
                    <div class="card-body">
                        <h5 class="card-title">Card title</h5>
                        <h6 class="card-subtitle mb-2 text-muted">Card subtitle</h6>
                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the
                            card's content.</p>
                        <a href="#" class="card-link">Card link</a>
                        <a href="#" class="card-link">Another link</a>
                    </div>
    </div>
    
    
    `
});
Vue.component('post', {
    template: `
    <div>
    <div class="card gedf-card">
                    <div class="card-header">
                        <div class="d-flex justify-content-between align-items-center">
                            <div class="d-flex justify-content-between align-items-center">
                                <div class="mr-2">
                                    <img class="rounded-circle" width="45" src="https://picsum.photos/50/50" alt="">
                                </div>
                                <div class="ml-2">
                                    <div class="h5 m-0">@LeeCross</div>
                                    <div class="h7 text-muted">Miracles Lee Cross</div>
                                </div>
                            </div>
                            <div>
                                <div class="dropdown">
                                    <button class="btn btn-link dropdown-toggle" type="button" id="gedf-drop1" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                        <i class="fa fa-ellipsis-h"></i>
                                    </button>
                                    <div class="dropdown-menu dropdown-menu-right" aria-labelledby="gedf-drop1">
                                        <div class="h6 dropdown-header">Configuration</div>
                                        <a class="dropdown-item" href="#">Save</a>
                                        <a class="dropdown-item" href="#">Hide</a>
                                        <a class="dropdown-item" href="#">Report</a>
                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>
                    <div class="card-body">
                        <div class="text-muted h7 mb-2"> <i class="fa fa-clock-o"></i> 10 min ago</div>
                        <a class="card-link" href="#">
                            <h5 class="card-title"> Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit consectetur
                                deserunt illo esse distinctio.</h5>
                        </a>

                        <p class="card-text">
                            Lorem ipsum dolor sit amet consectetur adipisicing elit. Magnam omnis nihil, aliquam est, voluptates officiis iure soluta
                            alias vel odit, placeat reiciendis ut libero! Quas aliquid natus cumque quae repellendus. Lorem
                            ipsum dolor sit amet consectetur adipisicing elit. Ipsa, excepturi. Doloremque, reprehenderit!
                            Quos in maiores, soluta doloremque molestiae reiciendis libero expedita assumenda fuga quae.
                            Consectetur id molestias itaque facere? Hic!
                        </p>
                        <div>
                            <span class="badge badge-primary">JavaScript</span>
                            <span class="badge badge-primary">Android</span>
                            <span class="badge badge-primary">PHP</span>
                            <span class="badge badge-primary">Node.js</span>
                            <span class="badge badge-primary">Ruby</span>
                            <span class="badge badge-primary">Paython</span>
                        </div>
                    </div>
                    <div class="card-footer">
                        <a href="#" class="card-link"><i class="fa fa-gittip"></i> Like</a>
                        <a href="#" class="card-link"><i class="fa fa-comment"></i> Comment</a>
                        <a href="#" class="card-link"><i class="fa fa-mail-forward"></i> Share</a>
                    </div>
                </div>

    </div>
    `

});

Vue.component('create-post', {
    template: 
    `
    <div>
    <div class="col-lg gedf-main">

                
                <div class="card gedf-card">
                    <div class="card-header">
                        <ul class="nav nav-tabs card-header-tabs" id="myTab" role="tablist">
                            <li class="nav-item">
                                <a class="nav-link active" id="posts-tab" data-toggle="tab" href="#posts" role="tab" aria-controls="posts" aria-selected="true">Make
                                    a publication</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" id="images-tab" data-toggle="tab" role="tab" aria-controls="images" aria-selected="false" href="#images">Images</a>
                            </li>
                        </ul>
                    </div>
                    <div class="card-body">
                        <div class="tab-content" id="myTabContent">
                            <div class="tab-pane fade show active" id="posts" role="tabpanel" aria-labelledby="posts-tab">
                                <div class="form-group">
                                    <label class="sr-only" for="message">post</label>
                                    <textarea class="form-control" id="message" rows="3" placeholder="What are you thinking?"></textarea>
                                </div>

                            </div>
                            <div class="tab-pane fade" id="images" role="tabpanel" aria-labelledby="images-tab">
                                <div class="form-group">
                                    <div class="custom-file">
                                        <input type="file" class="custom-file-input" id="customFile">
                                        <label class="custom-file-label" for="customFile">Upload image</label>
                                    </div>
                                </div>
                                <div class="py-4"></div>
                            </div>
                        </div>

                        <div class="btn-toolbar justify-content-between">
                            <div class="btn-group">
                                <button type="submit" class="btn btn-theme text-white">share</button>
                            </div>
                           
                        </div>

                    
                </div>
        </div> 
    </div>
    `
});

Vue.component('profile-popup', {
    template: `
    <div>
        <div class="container-fluid gedf-wrapper ">
            <div> 
                     <h6> This is a profile pop up </h6>
            </div>
            
        </div>
     </div>
    `

});

const Dashboard = Vue.component('dashboard', {
    template: `
    <div>
                <dash-header> </dash-header>

            <div class = "d-flex flex-row"> 
                <div>
                    <profile-popup> </profile-popup>
                </div>

                <div class = "">
                    <div >
                        <create-post> </create-post>
                    </div>

                    <div class= "col-md-8">

                        <post> </post>                  
                         <post> </post>
                    </div>

                        
                    
                </div>

                            
                <div class="col-md-3 d-flex flex-column">
                    <card></card>
                    <card> </card>
                </div>

            </div>
            
    </div>
    `,
    data: function () {

        return {
            showLogin: false
        }
    },
    methods: {

        SwitchFile: function () {

            fetch('api/dashboard', {
                method: 'POST',



            });

        }
    }


});


// Define Routes
const router = new VueRouter({
    mode: 'history',
    routes: [
        // { path: "/Home", component: Home },
        // Put other routes here
        { path: "/login", component: Login },

        { path: "/", component: Login },

        { path: "/signup", component: SignUp },

        { path: "/dashboard", component: Dashboard },
        // This is a catch all route in case none of the above matches
        { path: "*", component: NotFound }


    ]
});

// Instantiate our main Vue Instance
let app = new Vue({
    el: "#app",
    router
});
>>>>>>> parent of e6c88c3... Dashboard in progress


/* Add your Application JavaScript */
Vue.component('app-header', {
    template: `
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
    `,

    data: function () {
        return {


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

Vue.component('sidebar', {
    template: `
    
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
        <div class="page">
      <!-- Main Navbar-->
      <header class="header ">
        <nav class="navbar bg-theme">
          <!-- Search Box-->
          <div class="search-box">
            <button class="dismiss"><i class="icon-close"></i></button>
            <form id="searchForm" action="#" role="search">
              <input type="search" placeholder="What are you looking for..." class="form-control">
            </form>
          </div>
          <div class="container-fluid">
            <div class="navbar-holder d-flex align-items-center justify-content-between">
              <!-- Navbar Header-->
              <div class="navbar-header">
                <!-- Navbar Brand --><a href="index.html" class="navbar-brand d-none d-sm-inline-block">
                  <div class="brand-text d-none d-lg-inline-block"><span>MyBook</span><strong>Dashboard</strong></div>
                  <div class="brand-text d-none d-sm-inline-block d-lg-none"><strong>BD</strong></div></a>
                <!-- Toggle Button--><a id="toggle-btn" href="#" class="menu-btn active"><span></span><span></span><span></span></a>
              </div>
              <!-- Navbar Menu -->
              <ul class="nav-menu list-unstyled d-flex flex-md-row align-items-md-center">
                <!-- Search-->
                <li class="nav-item d-flex align-items-center"><a id="search" href="#"><i class="icon-search"></i></a></li>
                <!-- Notifications-->
                <li class="nav-item dropdown"> <a id="notifications" rel="nofollow" data-target="#" href="#" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="nav-link"><i class="fa fa-bell-o"></i><span class="badge bg-red badge-corner">12</span></a>
                  <ul aria-labelledby="notifications" class="dropdown-menu">
                    <li><a rel="nofollow" href="#" class="dropdown-item"> 
                        <div class="notification">
                          <div class="notification-content"><i class="fa fa-envelope bg-green"></i>You have 6 new messages </div>
                          <div class="notification-time"><small>4 minutes ago</small></div>
                        </div></a></li>
                    <li><a rel="nofollow" href="#" class="dropdown-item"> 
                        <div class="notification">
                          <div class="notification-content"><i class="fa fa-twitter bg-blue"></i>You have 2 followers</div>
                          <div class="notification-time"><small>4 minutes ago</small></div>
                        </div></a></li>
                    <li><a rel="nofollow" href="#" class="dropdown-item"> 
                        <div class="notification">
                          <div class="notification-content"><i class="fa fa-upload bg-orange"></i>Server Rebooted</div>
                          <div class="notification-time"><small>4 minutes ago</small></div>
                        </div></a></li>
                    <li><a rel="nofollow" href="#" class="dropdown-item"> 
                        <div class="notification">
                          <div class="notification-content"><i class="fa fa-twitter bg-blue"></i>You have 2 followers</div>
                          <div class="notification-time"><small>10 minutes ago</small></div>
                        </div></a></li>
                    <li><a rel="nofollow" href="#" class="dropdown-item all-notifications text-center"> <strong>view all notifications                                            </strong></a></li>
                  </ul>
                </li>
                <!-- Messages                        -->
                <li class="nav-item dropdown"> <a id="messages" rel="nofollow" data-target="#" href="#" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="nav-link"><i class="fa fa-envelope-o"></i><span class="badge bg-orange badge-corner">10</span></a>
                  <ul aria-labelledby="notifications" class="dropdown-menu">
                    <li><a rel="nofollow" href="#" class="dropdown-item d-flex"> 
                        <div class="msg-profile"> <img src="img/avatar-1.jpg" alt="..." class="img-fluid rounded-circle"></div>
                        <div class="msg-body">
                          <h3 class="h5">Jason Doe</h3><span>Sent You Message</span>
                        </div></a></li>
                    <li><a rel="nofollow" href="#" class="dropdown-item d-flex"> 
                        <div class="msg-profile"> <img src="img/avatar-2.jpg" alt="..." class="img-fluid rounded-circle"></div>
                        <div class="msg-body">
                          <h3 class="h5">Frank Williams</h3><span>Sent You Message</span>
                        </div></a></li>
                    <li><a rel="nofollow" href="#" class="dropdown-item d-flex"> 
                        <div class="msg-profile"> <img src="img/avatar-3.jpg" alt="..." class="img-fluid rounded-circle"></div>
                        <div class="msg-body">
                          <h3 class="h5">Ashley Wood</h3><span>Sent You Message</span>
                        </div></a></li>
                    <li><a rel="nofollow" href="#" class="dropdown-item all-notifications text-center"> <strong>Read all messages   </strong></a></li>
                  </ul>
                </li>
               
                <!-- Logout    -->
                <li class="nav-item"><a href="login.html" class="nav-link logout"> <span class="d-none d-sm-inline">Logout</span><i class="fa fa-sign-out"></i></a></li>
              </ul>
            </div>
          </div>
        </nav>
      </header>
      <div class="page-content d-flex align-items-stretch"> 
        <!-- Side Navbar -->
        <nav class="side-navbar">
          <!-- Sidebar Header-->
          <div class="sidebar-header d-flex align-items-center">

          <!-- ADD PHOTO- CONNECT DATABASE to get info-->
            <!-- <div class="avatar"><img src="" alt="..." class="img-fluid rounded-circle"></div> -->
            <div class="title">
              <h1 class="h4"> Username</h1>
             
            </div>
          </div>
          <!-- Sidebar Navidation Menus--><span class="heading">Main</span>
          <ul class="list-unstyled">
            <li class="active"><a href="index.html"> <i class="icon-home"></i>Home </a></li>
            <li><a href="tables.html"> <i class="icon-grid"></i>My Profile </a></li>
            <li><a href="charts.html"> <i class="fa fa-bar-chart"></i>My Groups </a></li>
            <li><a href="forms.html"> <i class="icon-padnote"></i>My Friends</a></li>
            <li><a href="#exampledropdownDropdown" aria-expanded="false" data-toggle="collapse">Example dropdown </a>
              <ul id="exampledropdownDropdown" class="collapse list-unstyled ">
                <li><a href="#">Page</a></li>
                <li><a href="#">Page</a></li>
                <li><a href="#">Page</a></li>
              </ul>
            </li>
            
          </ul>
         
        </nav>
        <div class="content-inner">
          <!-- Page Header-->
          <header class="page-header">
            <div class="container-fluid">
              <h2 class="no-margin-bottom">Dashboard</h2>
            </div>
          </header>
            
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

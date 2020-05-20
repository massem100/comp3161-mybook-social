
// var GroupResult = Vue.component('group-result', {
//     template: 
//     `
//     </div>
//     <div>
//         <div>
//             <form action  method='POST' class = "">
                
//                 <div class="searchContainer">
//                     <i class="fa fa-search searchIcon"></i>
//                     <input type= "text" class="searchBox" placeholder="Search by Group name">
                    
//                     <input type="submit" value="Search" class="searchButton">
//                 </div>
//             </form>
//         </div>
        
//         <div class = "d-flex flex-row mr-2">           
          
//             <div class="d-flex flex-column bg-light border col-lg-8 rounded ml-0 mt-3 mr-2">
//                 <h5 class="font-weight-bold m-2 text-primary "> Search Results for Groups</h5>
//                 <p class="text-center text-secondary"> No Searches made yet</p>
                
//                 <ul class="list-group border rounded bg-light">
                
//                     <div class="list-group-item  d-flex flex-row">
//                         <div> 
//                         <h6> placeholder for group</h6>
//                         </div>
//                         <div class="ml-auto">
//                             <button id="friendsbtn" class="btn btn-primary rounded"> Join Group</button>
//                         </div>
                
//                     </div>
                
//                 </ul>
                
//             </div>
            
        
           
//             <div class = " card w-100 mt-3 ml-1 mr-1 mb-2 bg-light">
//                 <div class="card-header bg-primary text-white">
//                     <h5> Your Active Groups</h5>
//                 </div>
//             </div>
            

//         </div>
        
//     </div>
//     </div>
    
//     `, 
//     data: function() {
//         return {
//             name: "BOMBBB",
//         }
//     }, 
//     created: function () {
//         let self = this;
//         fetch("/api/searchgroup", {
//             method: "GET",
//             dataType: "html",
//             headers: {
//                 "X-CSRFToken": token,
//             },
//             credentials: "same-origin",
//             })
//             .then(function (response) {
//                 return response.json();
//             })
//             .then(function (jsonResponse) {
//                 // display a success message
//                 console.log(jsonResponse);  
//             })
//             .catch(function (error) {
//                 // console.log(error);
//             });
//     }
// });




// let app = new Vue({
//     el: "#app",
//     components: {
//         'group-result': GroupResult
//     },
// });
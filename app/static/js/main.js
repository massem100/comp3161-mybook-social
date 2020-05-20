
var GroupResult = Vue.component('group-result', {
    template: 
    `
    <div> 
        <h4> This is my {{name}} vue component! </h4>
    </div>
    `, 
    data: function() {
        return {
            name: "BOMBBB",
        }
    }
});




let app = new Vue({
    el: "#app",
    components: {
        'group-result': GroupResult
    },
});
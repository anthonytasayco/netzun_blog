new Vue({
  delimiters: ['#{', '}'],
  el: '#blog',
    template: `
    <div>
        <h1>BLOG: Lista de Publicaciones</h1>
        <div>
            <ul>
                <li v-for="item in posts">
                    <h3>#{item.name}</h3>
                    <h4>#{item.created_date}</h4>
                    <img :src="item.image" width="300" height="200" alt=""/>
                    <p>#{item.description}</p>
                </li>
            </ul>
        </div>
    </div>
    `,
    data() {
        return {
            posts: []
        }
    },
    methods:{
    get_items(url){
        axios.get('/api_v1/')
        .then((res)=>{
            let data = res.data;
            this.posts = res.data
            console.log(data, '<----------DATA')
        }).catch((error)=>{

        });
    }

    },
    computed:{},
    mounted() {
        this.get_items(this.url);
    }
})
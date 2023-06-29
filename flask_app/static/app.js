const search = document.querySelector("search")

search.addEventListener("keyup", handleSearch)

const NewsAPI = require('newsapi');
const newsapi = new NewsAPI('8e4c8f54ae49478d81dbd895ba406409');

newsapi.v2.topHeadlines({
    sources: 'bbc-news,the-verge',
    q: 'bitcoin',
    category: 'business',
    language: 'en',
    country: 'us'
    }).then(response => {
    console.log(response);});

    function getNews(){
        fetch('https://newsapi.org/v2/top-headlines -G')
            .then( response => response.json() )
            .then( data => console.log(data) )
    }
    // Prints out { message : "Hello World" }
    getNews();

function handleSearch(event) {
    const searchString = event.target.value;
    if(searchString !== "") {
        dropdownMenu.classList.add("show")
    } else {
        // dropdownMenu.classList.remove("show")
    }
}

function search(e){
    e.preventDefault();
    var searchForm = document.getElementById('searchForm')
    var form = new FormData(searchForm);
    fetch('https://newsapi.org/v2/top-headlines -G',{method:'POST',body:form})
        .then(res => res.json() )
        .then( data => console.log(data) )
}

async function getNews() {
        const response = await fetch(apiURL + `&appid=${apiKey}`);
    // We then need to convert the data into JSON format.
    var news = await response.json();
    return news;
}
    
console.log(news);

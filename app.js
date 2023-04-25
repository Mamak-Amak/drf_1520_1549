import React from 'react';
import axios from 'axios'
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js'
import { BrowserRouter, Route, Switch, Redirect, Link } from 'react-router-dom'

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'authors': []
        }
    }
    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/authors')
            .then(Response => {
                const authors = Response.data
                this this.setState(
                    {
                        'authors': authors
                    }
                )
            }).catch(error => console.log(error))

    }
    
    
render() {
    return (
        <div>
            <AuthorList authors={this.state.authors} />
        </div>
    )
}
}

export default App;

import React from 'react'
import AuthorList from './components/Author.js'
import BookList from './components/Book.js'
import {HashRouter, Route, Link, Switch} from 'react-router-dom'
import {HashRouter, Route, Link, Switch, Redirect} from 'react-router-dom'


class App extends React.Component {
    constructor(props) {
        super(props)
        const author1 = {id: 1, name: 'Грин', birthday_year: 1880}
        const author2 = {id: 2, name: 'Пушкин', birthday_year: 1799}
        const authors = [author1, author2]
        const book1 = {id: 1, name: 'Алые паруса', author: author1}
        const book2 = {id: 2, name: 'Золотая цепь', author: author1}
        const book3 = {id: 3, name: 'Пиковая дама', author: author2}
        const book4 = {id: 4, name: 'Руслан и Людмила', author: author2}
        const books = [book1, book2, book3, book4]
        this.state = {
            'authors': authors,
            'books': books

    createBook(name, author) {
                const headers = this.get_headers()
                const data = { name: name, author: author }
                axios.post(`http://127.0.0.1:8000/api/books/`, data, { headers, headers })
                    .then(response => {
                        let new_book = response.data
                        const author = this.state.authors.filter((item) => item.id ===
                            new_book.author)[0]
                        new_book.author = author
                        this.setState({ books: [...this.state.books, new_book] })
                    }).catch(error => console.log(error))
            }
    
    deleteBook(id) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/books/${id}`, { headers, headers })
            .then(response => {
                this.setState({books: this.state.books.filter((item) => item.id !==id)
                        })
                    }).catch(error => console.log(error))
}
}
    render() {
    return (
        <div className="App">
        <HashRouter>
                <Route exact path='/' component={() => <AuthorList
items={this.state.authors} />} />
                <Route exact path='/books' component={() => <BookList
items={this.state.books} />} />
        </HashRouter>
        </div>
)
}
}
export default App;
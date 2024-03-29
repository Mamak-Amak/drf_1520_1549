import React from 'react'
const BookItem = ({ item, deleteBook }) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.name}</td>
            <td>{item.author.name}</td>
            <td><button onClick={() => deleteBook(item.id)}
                type='button'>Delete</button></td>
        </tr>
    )
}
const BookList = ({ items, deleteBook }) => {
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>NAME</th>
                <th>AUHTOR</th>
                <th></th>
            </tr>
            {items.map((item) => <BookItem item={item} deleteBook={deleteBook}
            />)}
        </table>
    )
}
export default BookList
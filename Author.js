import React from "react";
const AuthorItem = ({ item }) => {
  return (
    <tr>
      <td>{item.id}</td>
      <td>{item.name}</td>
      <td>{item.birthday_year}</td>
    </tr>
  );
};

const AuthorList = ({ items }) => {
  return (
    <table>
      <tr>
        <th>ID</th>
        <th>NAME</th>
        <th>BIRTHDAY_YEAR</th>
      </tr>
      {items.map((item) => (
        <AuthorItem item={item} />
      ))}
    </table>
  );
};
export default AuthorList;

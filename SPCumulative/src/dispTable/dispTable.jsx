import "./dispTable.css";
import React from "react";
import Table from "rc-table";

function template() {
  return (
    <div className="disp-table">
      <h1>{"S&P 500 Total Returns by Year"}</h1>
      <Table
        className="table table-hover"
        columns={this.state.columns}
        data={this.displayData()}
      />
    </div>
  );
}

export default template;

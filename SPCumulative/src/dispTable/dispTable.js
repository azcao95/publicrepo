import React from "react";
import template from "./dispTable.jsx";

class dispTable extends React.Component {
  displayData() {
    let dispData = [];
    let cumulativeReturn = 1;

    for (let i = this.props.startDate; i <= this.props.endDate; i++) {
      cumulativeReturn *= (100 + parseFloat(this.props.data[i])) / 100;
      let dispCumulativeReturn = (100 * cumulativeReturn - 100).toFixed(2);

      if (dispCumulativeReturn > 0) {
        dispCumulativeReturn = "+" + dispCumulativeReturn;
      }

      dispData.push({
        year: i,
        totalReturn: this.props.data[i],
        cumulativeReturn: dispCumulativeReturn,
      });
    }

    return dispData.reverse();
  }

  constructor(props) {
    super(props);

    console.log(this.props.data);

    const dispColumns = [
      {
        title: "Year",
        dataIndex: "year",
        key: "year",
        align: "left",
      },
      {
        title: "Total Return",
        dataIndex: "totalReturn",
        key: "totalReturn",
        align: "left",
      },
      {
        title: "Cumulative Return",
        dataIndex: "cumulativeReturn",
        key: "cumulativeReturn",
        align: "left",
      },
    ];

    this.state = {
      columns: dispColumns,
    };
  }

  render() {
    return template.call(this);
  }
}

export default dispTable;

import React from 'react';
import { Radar } from "react-chartjs-2"




function Graph({legend, values}) {

    console.log(values);

    const datasets = [
        {
          label: legend,
          data: values,
          fill: false,
          backgroundColor: "rgb(245, 245, 245)",
          borderColor: "rgba(245, 124, 0, 1)",
          pointBackgroundColor: "rgba(245, 124, 0, 1)",
          pointBorderColor: "#fff",
          pointHoverBackgroundColor: "rgb(245, 245, 245)",
          pointHoverBorderColor: "rgb(245, 245, 245)",
          hoverBackgroundColor: "rgb(245, 245, 245)"
        }
      ];

    const data = {labels: ['Вовлеченность','Обучаемость','Организованность','Командность'], datasets};
    const chartOptions = {
        scale: {
          ticks: {
            min: -1,
            max: 3,
          },
          pointLabels: {
            fontSize: 18
          }
        },
    };      

    return (
      <div style={{"display":"block", "width":"520px", "height":"420"}}>
        <Radar
        type='radar'
         options={chartOptions} data={data}/>
         </div>
    );
}

export default Graph;
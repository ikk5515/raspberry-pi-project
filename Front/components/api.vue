<template>
  <div>
    <h1>대기질 정보</h1>
    <div>
      <canvas ref="coChart" width="400" height="200"></canvas>
    </div>
  </div>
</template>

<script>
import Chart from 'chart.js';
import axios from 'axios';

export default {
  data() {
    return {
      airQualityData: {}
    };
  },
  mounted() {
    const apiUrl =`https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey=UG%2FoFdnta3Lg9FqBzA2vT8JPVkuPIX99gvnSZvXQ8aJnMRwzbLT6or1kf5l6bOSOSX2CgVF6MrBQqX7cgpybDA%3D%3D&returnType=xml&numOfRows=100&pageNo=1&stationName=%EC%A2%85%EB%A1%9C%EA%B5%AC&dataTerm=DAILY&ver=1.0`; // 여기에 실제 API URL을 입력하세요

    axios.get(apiUrl)
      .then(response => {
        const parser = new DOMParser();
        const xmlDoc = parser.parseFromString(response.data, 'text/xml');
        const items = xmlDoc.getElementsByTagName('item');

        const data = {};

        for (let i = 0; i < items.length; i++) {
          const item = items[i];
          const dataTime = item.getElementsByTagName('dataTime')[0].textContent;
          const measurements = {};

          const itemChildNodes = item.childNodes;
          for (let j = 0; j < itemChildNodes.length; j++) {
            const childNode = itemChildNodes[j];
            if (childNode.nodeType === 1 && childNode.nodeName !== 'dataTime') {
              measurements[childNode.nodeName] = childNode.textContent;
            }
          }

          data[dataTime] = measurements;
        }

        this.airQualityData = data;

        const coValues = [];
        const timeLabels = [];

        Object.keys(this.airQualityData).forEach(time => {
          timeLabels.push(time);
          coValues.push(parseFloat(this.airQualityData[time]['coValue']));
        });

        this.createChart(timeLabels, coValues);
      })
      .catch(error => {
        console.error(error);
      });
  },
  methods: {
    createChart(labels, coValues) {
      const ctx = this.$refs.coChart.getContext('2d');
      new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,
          datasets: [{
            label: 'CO 값',
            data: coValues,
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
          }]
        },
        options: {
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
    }
  }
};
</script>

<style>
/* 여기에 스타일을 추가하세요 */
</style>


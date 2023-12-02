<template>
  <div class="container">
    <h1>센서 값</h1>
    <div class="input-group">
      <select v-model="selectedSensor" class="select-sensor">
        <option v-for="sensor in sensorList" :key="sensor" :value="sensor">{{ sensor }}</option>
        <!-- 다른 센서 옵션을 추가 -->
      </select>
      <button @click="getData" class="get-data-button">Get Data</button>
    </div>
    <div v-if="responseData" class="chart-container">
      <canvas ref="chartCanvas" class="chart-canvas"></canvas>
    </div>

    <!-- 싸이클 POST -->
    <div class="input-group">
      <label for="cycleValue">Cycle Value:</label>
      <input type="number" v-model="cycleValue" id="cycleValue" />
      <button @click="changeCycle" class="change-cycle-button">Change Cycle</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Chart from 'chart.js/auto';

export default {
  data() {
    return {
      selectedSensor: 'MQ5',
      responseData: null,
      chart: null,
      cycleValue: 3000,
      sensorList: [] // 센서 리스트를 저장할 배열 추가
    };
  },
  methods: {
    async getSensorList() {
      try {
        const response = await axios.get('https://port-0-raspberry-pi-project-5mk12alpbcv53c.sel5.cloudtype.app/sensors');
        this.sensorList = response.data;
      } catch (error) {
        console.error('Error fetching sensor list:', error);
      }
    },
    async getData() {
      try {
        const response = await axios.get(`https://port-0-raspberry-pi-project-5mk12alpbcv53c.sel5.cloudtype.app/sensors/graph/${this.selectedSensor}`);
        this.responseData = response.data;
        this.renderChart(); // 데이터를 가져온 후 차트를 렌더링
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    renderChart() {
      if (this.chart) {
        this.chart.destroy(); // 기존 차트 제거
      }
      const labels = [];
      const values = [];

      this.responseData.forEach(item => {
        const date = new Date(item.measure_time);
        const month = date.getMonth() + 1; // getMonth()는 0부터 시작하므로 +1.
        const day = date.getDate();
        const hours = date.getHours();
        const minutes = date.getMinutes();
        const seconds = date.getSeconds();
        
        labels.push(`${month}-${day} ${hours}:${minutes}:${seconds}`);
        values.push(item.measure_value);
      });

      const ctx = this.$refs.chartCanvas.getContext('2d');
      this.chart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,
          datasets: [
            {
              label: `${this.selectedSensor} Values`,
              data: values,
              backgroundColor: 'rgba(75, 192, 192, 0.2)',
              borderColor: 'rgba(75, 192, 192, 1)',
              borderWidth: 1
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false
        }
      });
    },
    async changeCycle() {
      try {
        const requestBody = {
          name: this.selectedSensor,
          cycle: this.cycleValue // 입력한 주기 값을 가져와 전송
        };

        const response = await axios.post('https://port-0-raspberry-pi-project-5mk12alpbcv53c.sel5.cloudtype.app/change', requestBody);
        console.log('POST 요청 성공:', response.data);

        // 싸이클 값을 변경하고 난 후, 다시 데이터를 가져오는 등 추가 작업 수행 가능
      } catch (error) {
        console.error('POST 요청 실패:', error);
      }
    }
  },
  mounted() {
    this.getSensorList(); // 마운트 시 센서 리스트를 가져옴
    this.getData();
  }
};
</script>

<style>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Arial', sans-serif;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
  text-align: center;
  margin-bottom: 20px;
  color: #333;
}

.input-group {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.select-sensor {
  flex: 1;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  outline: none;
}

.get-data-button {
  padding: 10px 20px;
  margin-left: 10px;
  border: none;
  border-radius: 4px;
  background-color: #4caf50;
  color: #fff;
  cursor: pointer;
  transition: background-color 0.3s;
}

.get-data-button:hover {
  background-color: #45a049;
}

.chart-container {
  border: 1px solid #ddd;
  padding: 20px;
  border-radius: 4px;
  background-color: #fff;
}
.chart-canvas {
  width: 100%; /* 차트 요소를 부모 요소의 100%로 설정 */
  height: 400px; /* 원하는 높이로 설정하세요 */
}
/* ... */
</style>

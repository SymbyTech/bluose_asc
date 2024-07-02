<template>
  <div class="container">
    <div class="hero">
      <h1>Real Time Sensor Display</h1>
      <div class="chart-container">
        <h3>Board 0 - Cameras</h3>
        <table style="width:100%">
          <tr>
            <td>Channel</td>
            <td>Voltage</td>
            <td>Current</td>
            <td>Watt</td>
            <td>Switch</td>
          </tr>
          <tr>
            <td>1</td>
            <td id="v1"></td>
            <td id="c1"></td>
            <td id="t1"></td>
            <td>
              <label class="switch">
                <input type="checkbox" id="toggle-b0-0" @change="toggle(0, 0, 'b0')" />
                <span class="slider round"></span>
              </label>
            </td>
          </tr>
          <tr>
            <td>2</td>
            <td id="v2"></td>
            <td id="c2"></td>
            <td id="t2"></td>
            <td>
              <label class="switch">
                <input type="checkbox" id="toggle-b0-1" @change="toggle(1, 0, 'b0')" />
                <span class="slider round"></span>
              </label>
            </td>
          </tr>
          <tr>
            <td>3</td>
            <td id="v3"></td>
            <td id="c3"></td>
            <td id="t3"></td>
            <td>
              <label class="switch">
                <input type="checkbox" id="toggle-b0-2" @change="toggle(2, 0, 'b0')" />
                <span class="slider round"></span>
              </label>
            </td>
          </tr>
          <tr>
            <td>4</td>
            <td id="v4"></td>
            <td id="c4"></td>
            <td id="t4"></td>
            <td>
              <label class="switch">
                <input type="checkbox" id="toggle-b0-3" @change="toggle(3, 0, 'b0')" />
                <span class="slider round"></span>
              </label>
            </td>
          </tr>
        </table>

        <h3>Board 1 - LEDS</h3>
        <table style="width:100%">
          <tr>
            <td>Channel</td>
            <td>Voltage</td>
            <td>Current</td>
            <td>Watt</td>
            <td>Switch</td>
          </tr>
          <tr>
            <td>LED 1</td>
            <td id="v11-0-1"></td>
            <td id="c11-0-1"></td>
            <td id="t11-0-1"></td>
            <td>
              <label class="switch">
                <input type="checkbox" id="toggle-b1-0" @change="toggle(0, 1, 'b1')" />
                <span class="slider round"></span>
              </label>
            </td>
          </tr>
          <tr>
            <td>LED 2</td>
            <td id="v12-0-1"></td>
            <td id="c12-0-1"></td>
            <td id="t12-0-1"></td>
            <td>
              <label class="switch">
                <input type="checkbox" id="toggle-b1-1" @change="toggle(1, 1, 'b1')" />
                <span class="slider round"></span>
              </label>
            </td>
          </tr>
          <tr>
            <td>LED 3</td>
            <td id="v13-0-1"></td>
            <td id="c13-0-1"></td>
            <td id="t13-0-1"></td>
            <td>
              <label class="switch">
                <input type="checkbox" id="toggle-b1-2" @change="toggle(2, 1, 'b1')" />
                <span class="slider round"></span>
              </label>
            </td>
          </tr>
          <tr>
            <td>LED 4</td>
            <td id="v14-0-1"></td>
            <td id="c14-0-1"></td>
            <td id="t14-0-1"></td>
            <td>
              <label class="switch">
                <input type="checkbox" id="toggle-b1-3" @change="toggle(3, 1, 'b1')" />
                <span class="slider round"></span>
              </label>
            </td>
          </tr>
        </table>

        <h3>Board 2 - Motors</h3>
        <table style="width:100%">
          <tr>
            <td>Channel</td>
            <td>Voltage</td>
            <td>Current</td>
            <td>Watt</td>
            <td>Switch</td>
          </tr>
          <tr>
            <td>PORT Motor</td>
            <td id="v111"></td>
            <td id="c111"></td>
            <td id="t111"></td>
            <td>
              <label class="switch">
                <input type="checkbox" id="toggle-b2-0" @change="toggle(0, 2, 'b2')" />
                <span class="slider round"></span>
              </label>
            </td>
          </tr>
          <tr>
            <td>STBD Motor</td>
            <td id="v122"></td>
            <td id="c122"></td>
            <td id="t122"></td>
            <td>
              <label class="switch">
                <input type="checkbox" id="toggle-b2-1" @change="toggle(1, 2, 'b2')" />
                <span class="slider round"></span>
              </label>
            </td>
          </tr>
          <tr>
            <td>3</td>
            <td id="v133"></td>
            <td id="c133"></td>
            <td id="t133"></td>
            <td>
              <label class="switch">
                <input type="checkbox" id="toggle-b2-2" @change="toggle(2, 2, 'b2')" />
                <span class="slider round"></span>
              </label>
            </td>
          </tr>
          <tr>
            <td>4</td>
            <td id="v144"></td>
            <td id="c144"></td>
            <td id="t144"></td>
            <td>
              <label class="switch">
                <input type="checkbox" id="toggle-b2-3" @change="toggle(3, 2, 'b2')" />
                <span class="slider round"></span>
              </label>
            </td>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HelloWorld',
  methods: {
    async toggle(channel, board, id) {
      const state = document.getElementById(`toggle-${id}-${channel}`).checked ? 1 : 0;
      try {
        const response = await axios.post('http://127.0.0.1:8000/led_toggle', {
          led_channel: channel,
          state: state,
        });
        console.log(response.data);
      } catch (error) {
        console.error('Error toggling LED:', error);
      }
    },
  },
};
</script>

<style scoped>
.container {
  width: 100%;
  margin: 0 auto;
}

.hero {
  text-align: center;
}

.chart-container {
  margin-top: 20px;
}

table {
  width: 100%;
  margin-top: 20px;
  border-collapse: collapse;
}

td {
  padding: 10px;
  border: 1px solid #ccc;
}

.switch {
  position: relative;
  display: inline-block;
  width: 34px;
  height: 20px;
}

.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  transition: 0.4s;
}

.slider:before {
  position: absolute;
  content: '';
  height: 14px;
  width: 14px;
  left: 3px;
  bottom: 3px;
  background-color: white;
  transition: 0.4s;
}

input:checked + .slider {
  background-color: #2196f3;
}

input:checked + .slider:before {
  transform: translateX(14px);
}

.slider.round {
  border-radius: 34px;
}

.slider.round:before {
  border-radius: 50%;
}
</style>

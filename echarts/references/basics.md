# Echarts - Basics

**Pages:** 11

---

## Get Apache ECharts

**URL:** https://echarts.apache.org/handbook/en/basics/download/

**Contents:**
- Get Apache ECharts
- Installation
  - Install From npm
  - Use From CDN
  - Download From GitHub
  - Online Customization

Get Apache ECharts Apache ECharts offers a variety of installation options, so you can choose any of the following options depending on your project. Install From npm Use From CDN Download From GitHub Online Customization We'll go over each of these installation methods and the directory structure after download. Installation Install From npm npm install echarts   See Import ECharts for details on usage. Use From CDN ECharts is available on the following free CDNs: jsDelivr unpkg cdnjs Download From GitHub You can find links to each version on the releases page of the apache/echarts project. Click on the Source code under Assets at the bottom of the desired release version. After downloading, unzip the file and locate echarts.js file in the dist folder to include the full ECharts functionality. Online Customization If you want to introduce only some modules to reduce package size, you can use the ECharts online customization function to create a customized download of ECharts.

---

## Get Help

**URL:** https://echarts.apache.org/handbook/en/basics/help/

**Contents:**
- Get Help
- Technical Problems
  - Make sure that existing documentation do not solve your problem
  - Create the Minimal Reproducible Demo
  - Determining if It's a Bug
- Non-technical questions

Get Help Technical Problems Make sure that existing documentation do not solve your problem ECharts has a very large number of users, so it's more than likely that someone else has encountered and solved the problem you've had. By reading the documentation and using the search engine, you can solve your problem quickly by yourself without help from the community. Therefore, before doing anything else, make sure that current documentation and other resources can't solve your problem. Resources that can be helpful for you include, API Option Manual - you can try to use the search function Articles in this handbook FAQ Searching in GitHub issue Using the search engine Create the Minimal Reproducible Demo Create an example on Official Editor, CodePen, CodeSandbox or JSFiddle, which will make it easier for others to reproduce your problem. The example should reproduce your problem in the simplest way. Removing unnecessary code and data can enable those who want to help you to locate and then solve the problem more quickly. Please refer to How to Create a Minimal, Reproducible Example for more details. Determining if It's a Bug Report a Bug or Request a New Feature If some behavior is different from the documentation or isn't what you expected, it's probably a bug. If it's a bug, or you have a feature request, please use the issue template to create a new issue and describe it in detail as per the prompts. How-To Questions If it's not a bug, but you don't know how to achieve something, try the stackoverflow.com If you don't get an answer, you can also send an email to dev@echarts.apache.org. In order for more people to understand your question and to get help in future searches, it is highly recommended to write the email in English. Non-technical questions For other non-technical questions, you can send an email in English to dev@echarts.apache.org.

---

## Using ECharts as an NPM Package

**URL:** https://echarts.apache.org/handbook/en/basics/import/

**Contents:**
- Using ECharts as an NPM Package
- Install ECharts via NPM
- Import All ECharts Functionality
- Shrinking Bundle Size
- Creating an Option Type in TypeScript

Using ECharts as an NPM Package There are two approaches to using ECharts as a package. The simplest approach is to make all functionality immediately available by importing from echarts. However, it is encouraged to substantially decrease bundle size by only importing as necessary such as echarts/core and echarts/charts. Install ECharts via NPM You can install ECharts via npm using the following command npm install echarts   Import All ECharts Functionality To include all of ECharts, we simply need to import echarts. import * as echarts from 'echarts';

// Create the echarts instance
var myChart = echarts.init(document.getElementById('main'));

// Draw the chart
myChart.setOption({
  title: {
    text: 'ECharts Getting Started Example'
  },
  tooltip: {},
  xAxis: {
    data: ['shirt', 'cardigan', 'chiffon', 'pants', 'heels', 'socks']
  },
  yAxis: {},
  series: [
    {
      name: 'sales',
      type: 'bar',
      data: [5, 20, 36, 10, 10, 20]
    }
  ]
});   Shrinking Bundle Size The above code will import all the charts and components in ECharts, but if you don't want to bring in all the components, you can use the tree-shakeable interface provided by ECharts to bundle the required components and get a minimal bundle. // Import the echarts core module, which provides the necessary interfaces for using echarts.
import * as echarts from 'echarts/core';

// Import bar charts, all suffixed with Chart
import { BarChart } from 'echarts/charts';

// Import the title, tooltip, rectangular coordinate system, dataset and transform components
import {
  TitleComponent,
  TooltipComponent,
  GridComponent,
  DatasetComponent,
  TransformComponent
} from 'echarts/components';

// Features like Universal Transition and Label Layout
import { LabelLayout, UniversalTransition } from 'echarts/features';

// Import the Canvas renderer
// Note that including the CanvasRenderer or SVGRenderer is a required step
import { CanvasRenderer } from 'echarts/renderers';

// Register the required components
echarts.use([
  BarChart,
  TitleComponent,
  TooltipComponent,
  GridComponent,
  DatasetComponent,
  TransformComponent,
  LabelLayout,
  UniversalTransition,
  CanvasRenderer
]);

// The chart is initialized and configured in the same manner as before
var myChart = echarts.init(document.getElementById('main'));
myChart.setOption({
  // ...
});   Note that in order to keep the size of the package to a minimum, ECharts does not provide any renderer in the tree-shakeable interface, so you need to choose to import CanvasRenderer or SVGRenderer as the renderer. The advantage of this is that if you only need to use the SVG rendering mode, the bundle will not include the CanvasRenderer module, which is not needed. The "Full Code" tab on our sample editor page provides a very convenient way to generate a tree-shakable code. It will generate tree-shakable code based on the current option dynamically to use it directly in your project. Creating an Option Type in TypeScript For developers who are using TypeScript to develop ECharts, type interface is provided to create a minimal EChartsOption type. This type will be stricter than the default one provided because it will know exactly what components are being used. This can help you check for missing components or charts more effectively. import * as echarts from 'echarts/core';
import {
  BarChart,
  LineChart,
} from 'echarts/charts';
import {
  TitleComponent,
  TooltipComponent,
  GridComponent,
  // Dataset
  DatasetComponent,
  // Built-in transform (filter, sort)
  TransformComponent
} from 'echarts/components';
import { LabelLayout, UniversalTransition } from 'echarts/features';
import { CanvasRenderer } from 'echarts/renderers';
import type {
  // The series option types are defined with the SeriesOption suffix
  BarSeriesOption, 
  LineSeriesOption,
} from 'echarts/charts';
import type {
  // The component option types are defined with the ComponentOption suffix
  TitleComponentOption, 
  TooltipComponentOption,
  GridComponentOption,
  DatasetComponentOption
} from 'echarts/components';
import type { 
  ComposeOption, 
} from 'echarts/core';

// Create an Option type with only the required components and charts via ComposeOption
type ECOption = ComposeOption<
  | BarSeriesOption
  | LineSeriesOption
  | TitleComponentOption
  | TooltipComponentOption
  | GridComponentOption
  | DatasetComponentOption
>;

// Register the required components
echarts.use([
  TitleComponent,
  TooltipComponent,
  GridComponent,
  DatasetComponent,
  TransformComponent,
  BarChart,
  LineChart,
  LabelLayout,
  UniversalTransition,
  CanvasRenderer
]);

const option: ECOption = {
  // ...
};  

---

## Axis

**URL:** https://echarts.apache.org/handbook/en/concepts/axis/

**Contents:**
- Axis
- x-axis, y-axis
- Axis Line
- Tick
- Label
- Example

Axis The x/y-axis in the Cartesian coordinate system. x-axis, y-axis Both x-axis and y-axis included axis line, tick, label and title. Some chart will use the grid to assist the data viewing and calculating.  A normal 2D coordinate system has x-axis and y-axis. X-axis located at the bottom while y-axis at the left side in common. The Config is shown below: option = {
  xAxis: {
    // ...
  },
  yAxis: {
    // ...
  }
  // ...
};   The x-axis is usually used to declare the number of categories which was also called the aspects of observing the data: "Sales Time", "Sales Location" and "product name", etc.. The y-axis usually used to indicate the numerical value of categories. These data are used to examine the quantitative value of a certain type of data or some indicator you need to analyze, such as "Sales Quantity" and "Sales Price". option = {
  xAxis: {
    type: 'time',
    name: 'Sales Time'
    // ...
  },
  yAxis: {
    type: 'value',
    name: 'Sales Quantity'
    // ...
  }
  // ...
};   When x-axis has a large span, we can use the zoom method to display part of the data in the chart. option = {
  xAxis: {
    type: 'time',
    name: 'Sales Time'
    // ...
  },
  yAxis: {
    type: 'value',
    name: 'Sales Quantity'
    // ...
  },
  dataZoom: []
  // ...
};   In two-dimensional data, there can be more than two axes. There are usually two x or y axes at the same time in ECharts. You can change the config offset to avoid overlaps of axes at the same place. X-axes can be displayed at the top and bottom, y-axes at left and right. option = {
  xAxis: {
    type: 'time',
    name: 'Sales Time'
    // ...
  },
  yAxis: [
    {
      type: 'value',
      name: 'Sales Quantity'
      // ...
    },
    {
      type: 'value',
      name: 'Sales Price'
      // ...
    }
  ]
  // ...
};   Axis Line ECharts provide the config of axisLine. You can change the setting according to the demand, such as the arrow on two sides and the style of axes. option = {
  xAxis: {
    axisLine: {
      symbol: 'arrow',
      lineStyle: {
        type: 'dashed'
        // ...
      }
    }
    // ...
  },
  yAxis: {
    axisLine: {
      symbol: 'arrow',
      lineStyle: {
        type: 'dashed'
        // ...
      }
    }
  }
  // ...
};   Tick ECharts provide the config axisTick. You can change the setting according to the demand, such as the length of ticks, and the style of ticks. option = {
  xAxis: {
    axisTick: {
      length: 6,
      lineStyle: {
        type: 'dashed'
        // ...
      }
    }
    // ...
  },
  yAxis: {
    axisTick: {
      length: 6,
      lineStyle: {
        type: 'dashed'
        // ...
      }
    }
  }
  // ...
};   Label ECharts provide the config axisLabel. You can change the setting according to the demand, such as the text alignment and the customized label content. option = {
  xAxis: {
    axisLabel: {
      formatter: '{value} kg',
      align: 'center'
      // ...
    }
    // ...
  },
  yAxis: {
    axisLabel: {
      formatter: '{value} ¥',
      align: 'center'
      // ...
    }
  }
  // ...
};   Example The y-axis on the left side represents the monthly average temperature in Tokyo, the y-axis on the right side represents the precipitation of Tokyo. The x-axis represents the time. It reflects the trend and relation between the average temperature and precipitation. option = {
  tooltip: {
    trigger: 'axis',
    axisPointer: { type: 'cross' }
  },
  legend: {},
  xAxis: [
    {
      type: 'category',
      axisTick: {
        alignWithLabel: true
      },
      axisLabel: {
        rotate: 30
      },
      data: [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
      ]
    }
  ],
  yAxis: [
    {
      type: 'value',
      name: 'Precipitation',
      min: 0,
      max: 250,
      position: 'right',
      axisLabel: {
        formatter: '{value} ml'
      }
    },
    {
      type: 'value',
      name: 'Temperature',
      min: 0,
      max: 25,
      position: 'left',
      axisLabel: {
        formatter: '{value} °C'
      }
    }
  ],
  series: [
    {
      name: 'Precipitation',
      type: 'bar',
      yAxisIndex: 0,
      data: [6, 32, 70, 86, 68.7, 100.7, 125.6, 112.2, 78.7, 48.8, 36.0, 19.3]
    },
    {
      name: 'Temperature',
      type: 'line',
      smooth: true,
      yAxisIndex: 1,
      data: [
        6.0,
        10.2,
        10.3,
        11.5,
        10.3,
        13.2,
        14.3,
        16.4,
        18.0,
        16.5,
        12.0,
        5.2
      ]
    }
  ]
}; live   These are the concise intro of the usage of axis config. Check more details at: Official Website.

---

## Chart Container and Size

**URL:** https://echarts.apache.org/handbook/en/concepts/chart-size/

**Contents:**
- Chart Container and Size
- Initialization
  - Define a Parent Container in HTML
  - Specify the chart size
- Reactive of the Container Size
  - Listen to the Container Size to Change the Chart Size
  - State a Specific Chart Size
  - Dispose and Rebuild of the Container Node

Chart Container and Size In Get Started, we introduced the API to initialize the ECharts echarts.init. API Document has introduced the specific meaning of each parameters. Please read and understand the document before reading the following content. Refer to several common usage scenarios, here is the example to initialize a chart and change the size. Initialization Define a Parent Container in HTML In general, you need to define a <div> node and use the CSS to change the width and height. While initializing, import the chart into the node. Without declaring opts.width or opts.height, the size of the chart will default to the size of the node. <div id="main" style="width: 600px;height:400px;"></div>
<script type="text/javascript">
  var myChart = echarts.init(document.getElementById('main'));
</script>   To be noticed, before calling echarts.init, you need to make sure the container already has width and height. Specify the chart size If the height and width of the container do not exist, or you wish the chart size not equal to the container, you can initialize the size at the beginning. <div id="main"></div>
<script type="text/javascript">
  var myChart = echarts.init(document.getElementById('main'), null, {
    width: 600,
    height: 400
  });
</script>   Reactive of the Container Size Listen to the Container Size to Change the Chart Size In some cases, we want to accordingly change the chart size while the size of containers changed. For instance, the container has a height of 400px and a width of 100% site width. If you are willing to change the site width while stable the chart width as 100% of it, try the following method. You can listen to resize of the site to catch the event that the browser is resized. Then use echartsInstance.resize to resize the chart. <style>
  #main,
  html,
  body {
    width: 100%;
  }
  #main {
    height: 400px;
  }
</style>
<div id="main"></div>
<script type="text/javascript">
  var myChart = echarts.init(document.getElementById('main'));
  window.addEventListener('resize', function() {
    myChart.resize();
  });
</script>   Tips：Sometimes we may adjust the container size by JS/CSS, but this doesn't change the page size so that the resize event won't be triggered. You can try the ResizeObserver API to cover this scenario. State a Specific Chart Size Except for calling resize() without parameters, you can state the height and width to implement the chart size different from the size of the container. myChart.resize({
  width: 800,
  height: 400
});   Tips: Pay attention to how the API defined while reading the documentation. resize() API was sometimes mistaken for the form like myCharts.resize(800, 400) which do not exist. Dispose and Rebuild of the Container Node We assume that there exist several bookmark pages and each page contained some charts. In this case, the content in other pages will be removed in DOM when select one page. The user will not find the chart after reselecting these pages. Essentially, this is because the container node of the charts was removed. Even if the node is added again later, the node where the graph is located no longer exists. The correct way is, call echartsInstance.dispose to dispose the instance after the container was disposed, and call echarts.init to initialize after the container was added again. Tips: Call echartsInstance.dispose to release resources while disposing the node to avoid memory leaks.

---

## Dataset

**URL:** https://echarts.apache.org/handbook/en/concepts/dataset/

**Contents:**
- Dataset
- Define data under series
- Define data in dataset
- Map from Data to Chart
- Map Row or Column of dataset to series
- Dimension
- Map from Data to Charts (series.encode)
- Default series.encode
- Some Normal Settings of series.encode
- Visual Channel Mapping

Dataset dataset is a component dedicated to manage data. Although you can set the data in series.data for every series, we recommend you use the dataset to manage the data since ECharts 4 so that the data can be reused by multiple components and convenient for the separation of "data and configs". After all, data is the most common part to be changed while other configurations will mostly not change at runtime. Define data under series If data is defined under series, for example: option = {
  xAxis: {
    type: 'category',
    data: ['Matcha Latte', 'Milk Tea', 'Cheese Cocoa', 'Walnut Brownie']
  },
  yAxis: {},
  series: [
    {
      type: 'bar',
      name: '2015',
      data: [89.3, 92.1, 94.4, 85.4]
    },
    {
      type: 'bar',
      name: '2016',
      data: [95.8, 89.4, 91.2, 76.9]
    },
    {
      type: 'bar',
      name: '2017',
      data: [97.7, 83.1, 92.5, 78.1]
    }
  ]
}; live   Defining data under series is suitable for customization for some special data structures such as "tree", "graph" and large data.
However, it is not conducive to the data sharing for multiple series as well as mapping arrangement of chart types and series based on the original data. The other disadvantage is that programmers always need to divide the data in separate series (and categories) first. Define data in dataset Here are the advantages if you define data in dataset: Follow the ideas of data visualization: (I) Provide the data, (II)Mapping from data to visual to become a chart. Divide data from other configurations. The data often change but others not. It is
Easy to manage separately. Data can be reused by several series or component, you don't need to create copies of a large amount of data for every series. Support more common data format, such as a 2D array, array of classes, etc., to avoid users from converting for data format to a certain extent. Here is a simple dataset example: option = {
  legend: {},
  tooltip: {},
  dataset: {
    // Provide a set of data.
    source: [
      ['product', '2015', '2016', '2017'],
      ['Matcha Latte', 43.3, 85.8, 93.7],
      ['Milk Tea', 83.1, 73.4, 55.1],
      ['Cheese Cocoa', 86.4, 65.2, 82.5],
      ['Walnut Brownie', 72.4, 53.9, 39.1]
    ]
  },
  // Declare an x-axis (category axis).
  // The category map the first column in the dataset by default.
  xAxis: { type: 'category' },
  // Declare a y-axis (value axis).
  yAxis: {},
  // Declare several 'bar' series,
  // every series will auto-map to each column by default.
  series: [{ type: 'bar' }, { type: 'bar' }, { type: 'bar' }]
}; live   Or try to use the "array of classes" format: option = {
  legend: {},
  tooltip: {},
  dataset: {
    // Define the dimension of array. In cartesian coordinate system,
    // if the type of x-axis is category, map the first dimension to
    // x-axis by default, the second dimension to y-axis.
    // You can also specify 'series.encode' to complete the map
    // without specify dimensions. Please see below.

    dimensions: ['product', '2015', '2016', '2017'],
    source: [
      { product: 'Matcha Latte', '2015': 43.3, '2016': 85.8, '2017': 93.7 },
      { product: 'Milk Tea', '2015': 83.1, '2016': 73.4, '2017': 55.1 },
      { product: 'Cheese Cocoa', '2015': 86.4, '2016': 65.2, '2017': 82.5 },
      { product: 'Walnut Brownie', '2015': 72.4, '2016': 53.9, '2017': 39.1 }
    ]
  },
  xAxis: { type: 'category' },
  yAxis: {},
  series: [{ type: 'bar' }, { type: 'bar' }, { type: 'bar' }]
}; live   Map from Data to Chart The ideas of data visualization: (I) Provide the data, (II)Mapping from data to visual to become a chart. In short, you can set these configs of mapping: Specify 'column' or 'row' of dataset to map the series. You can use series.seriesLayoutBy to configure it. The default is to map according to the column. Rule of specifying dimension mapping: how to mapping from dimensions of 'dataset' to axis, tooltip, label and visualMap. To configure the mapping, please use series.encode and visualMap. The previous case did not give the mapping configuration so that ECharts will follow the default: if x-axis is category, mapping to the first row in dataset.source; three-column chart mapping with each row in dataset.source one by one. The details of the configuration are shown below: Map Row or Column of dataset to series Having the dataset, you can configure flexibly how the data map to the axis and series. You can use seriesLayoutBy to change the understanding of row and column of the chart. seriesLayoutBy can be: 'column': Default value. The series are placed above the column of dataset. 'row': The series are placed above the row of dataset. Check this case: option = {
  legend: {},
  tooltip: {},
  dataset: {
    source: [
      ['product', '2012', '2013', '2014', '2015'],
      ['Matcha Latte', 41.1, 30.4, 65.1, 53.3],
      ['Milk Tea', 86.5, 92.1, 85.7, 83.1],
      ['Cheese Cocoa', 24.1, 67.2, 79.5, 86.4]
    ]
  },
  xAxis: [
    { type: 'category', gridIndex: 0 },
    { type: 'category', gridIndex: 1 }
  ],
  yAxis: [{ gridIndex: 0 }, { gridIndex: 1 }],
  grid: [{ bottom: '55%' }, { top: '55%' }],
  series: [
    // These series will show in the first coordinate, each series map a row in dataset.
    { type: 'bar', seriesLayoutBy: 'row', xAxisIndex: 0, yAxisIndex: 0 },
    { type: 'bar', seriesLayoutBy: 'row', xAxisIndex: 0, yAxisIndex: 0 },
    { type: 'bar', seriesLayoutBy: 'row', xAxisIndex: 0, yAxisIndex: 0 },
    // These series will show in the second coordinate, each series map a column in dataset.
    { type: 'bar', seriesLayoutBy: 'column', xAxisIndex: 1, yAxisIndex: 1 },
    { type: 'bar', seriesLayoutBy: 'column', xAxisIndex: 1, yAxisIndex: 1 },
    { type: 'bar', seriesLayoutBy: 'column', xAxisIndex: 1, yAxisIndex: 1 },
    { type: 'bar', seriesLayoutBy: 'column', xAxisIndex: 1, yAxisIndex: 1 }
  ]
}; live   The effect of configuration is shown in this case. Dimension Most of the data described in commonly used charts is a "two-dimensional table" structure, in the previous case, we use a 2D array to contain a two-dimensional table. Now, when we map a series to a column, that column was called a "dimension" and each row was called "item", vice versa. The dimension can have their name to display in the chart. Dimension name can be defined in the first column (row). In the next case, 'score', 'amount', 'product' are the name of dimensions. The actual data locate from the second row. ECharts will automatically check if the first column (row) contained dimension name in dataset.source. You can also use dataset.sourceHeader: true to declare that the first column (row) represents the dimension name. Try to use single dataset.dimensions or some series.dimensions to define the dimensions, therefore you can specify the name and type together. var option1 = {
  dataset: {
    dimensions: [
      { name: 'score' },
      // can be abbreviated as 'string', to indicate dimension name
      'amount',
      // Specify dimensions in 'type'.
      { name: 'product', type: 'ordinal' }
    ],
    source: []
  }
  // ...
};

var option2 = {
  dataset: {
    source: []
  },
  series: {
    type: 'line',
    // series.dimensions will cover the config in dataset.dimension
    dimensions: [
      null, // use null if you do not want dimension name.
      'amount',
      { name: 'product', type: 'ordinal' }
    ]
  }
  // ...
};   In most cases, you don't need to define the dimension type because the ECharts will automatically judge it. If the judgment is inaccurate, you can define it manually. Dimension type can be the following values: 'number': Default, normal data. 'ordinal': String types data like categories, text can be used on the axis only with the dimension type 'ordinal'. ECharts will try to judge this type automatically but might be inaccurate, so you can specify manually. 'time': To represent time data, ECharts can automatically analyze data as timestamp if the dimension type is defined as 'time'. For instance, ECharts will auto-analyze if the data of this dimension is '2017-05-10'. If the dimension is used as time axis (axis.type = 'time'), the dimension type will also be 'time'. See data for more time type support. 'float': Use TypedArray to optimize the performance in 'float' dimension. 'int': Use TypedArray to optimize the performance in 'int' dimension. Map from Data to Charts (series.encode) After understand the concept of dimension, you can use series.encode to make a mapping: var option = {
  dataset: {
    source: [
      ['score', 'amount', 'product'],
      [89.3, 58212, 'Matcha Latte'],
      [57.1, 78254, 'Milk Tea'],
      [74.4, 41032, 'Cheese Cocoa'],
      [50.1, 12755, 'Cheese Brownie'],
      [89.7, 20145, 'Matcha Cocoa'],
      [68.1, 79146, 'Tea'],
      [19.6, 91852, 'Orange Juice'],
      [10.6, 101852, 'Lemon Juice'],
      [32.7, 20112, 'Walnut Brownie']
    ]
  },
  xAxis: {},
  yAxis: { type: 'category' },
  series: [
    {
      type: 'bar',
      encode: {
        // Map "amount" column to x-axis.
        x: 'amount',
        // Map "product" row to y-axis.
        y: 'product'
      }
    }
  ]
}; live   The basic structure of series.encode declaration: To the left of the colon: Specific name of axis or label. To the right of the colon: Dimension name (string) or number(int, count from 0), to specify one or several dimensions (using array). Generally, the following info is not necessary to be defined. Fill in as needed. Attribute suggested by series.encode // Supported in every coordinate and series:
encode: {
  // Display the value of dimension named "product" and "score" in tooltip.
  tooltip: ['product', 'score']
  // Connect dimension name of "Dimension 1" and "Dimension 3" as the series name. (Avoid to repeat longer names in series.name)
  seriesName: [1, 3],
  // Means to use the value in "Dimension 2" as the id. It makes the new and old data correspond by id
	// when using setOption to update data, so that it can show animation properly.
  itemId: 2,
  // The itemName will show in the legend of Pie Charts.
  itemName: 3
}

// Grid/cartesian coordinate unique configs:
encode: {
  // Map "Dimension 1", "Dimension 5" and "dimension named 'score'" to x-axis:
  x: [1, 5, 'score'],
  // Map "Dimension 0" to y-axis:
  y: 0
}

// singleAxis unique configs:
encode: {
  single: 3
}

// Polar coordinate unique configs:
encode: {
  radius: 3,
  angle: 2
}

// Geo-coordinate unique configs:
encode: {
  lng: 3,
  lat: 2
}

// For some charts without coordinate like pie chart, funnel chart:
encode: {
  value: 3
}   This is a richer example of series.encode. Default series.encode It is worth mentioning that ECharts will use some default mapping rules for some general charts (line, bar, scatter, candlestick, etc.) if series.encode is not specified. The default rule is: In coordinate system (e.g. Cartesian, Polar):
If there is category axis (axis.type = 'category'), map the first column(row) to the axis and each subsequent column(row) to each series. If both axes is not the category, then map every two columns in one series to two axes. Without axis (e.g. Pie Chart):
Use the first column(row) as the name, second column(row) as value. ECharts will not set the name if there is only one column(row). While the default rule cannot fulfill the requirements, you can configure encode by yourself, which is not complicate. Here is an example. Some Normal Settings of series.encode Q: How to set the 3rd column as x-axis, 5th column as y-axis? A: option = {
  series: {
    // dimensionIndex count from 0, so the 3rd line is dimensions[2].
    encode: { x: 2, y: 4 }
    // ...
  }
};   Q: How to set the 3rd row as x-axis, 5th row as y-axis? A: option = {
  series: {
    encode: { x: 2, y: 4 },
    seriesLayoutBy: 'row'
    // ...
  }
};   Q: How to set the 2nd column as a label? A:
We now support to trace value from specific dimension for label.formatter: series: {
  label: {
    // `'{@score}'` means the value in the dimension named "score".
    // `'{@[4]}'` means the value in dimension 4.
    formatter: 'aaa{@product}bbb{@score}ccc{@[4]}ddd';
  }
}   Q: How to show the 2nd and 3rd column in the tooltip? A: option = {
  series: {
    encode: {
      tooltip: [1, 2]
      // ...
    }
    // ...
  }
};   Q: How to define the dimension name if is not included in the dataset? A: var option = {
  dataset: {
    dimensions: ['score', 'amount'],
    source: [
      [89.3, 3371],
      [92.1, 8123],
      [94.4, 1954],
      [85.4, 829]
    ]
  }
};   Q: How to map the 3rd column to the size of the scatter chart? A: var option = {
  dataset: {
    source: [
      [12, 323, 11.2],
      [23, 167, 8.3],
      [81, 284, 12],
      [91, 413, 4.1],
      [13, 287, 13.5]
    ]
  },
  visualMap: {
    show: false,
    dimension: 2, // means the 3rd column
    min: 2, // lower bound
    max: 15, // higher bound
    inRange: {
      // Size of the bubble.
      symbolSize: [5, 60]
    }
  },
  xAxis: {},
  yAxis: {},
  series: {
    type: 'scatter'
  }
}; live   Q: I specified a mapping in encode, why it is not worked? A: Check your spelling, such as misspell the dimension name 'Life Expectancy' to 'Life Expectency' in encode. Visual Channel Mapping We can map visual channel by using visualMap. Check details in the visualMap document. Here is an example. Formats of Charts In most of the normal chart, the data is suitable to be described in the form of a two-dimensional table. That well-known software like 'MS Excel' and 'Numbers' all uses a two-dimensional table. Their data can be exported to JSON format and input to dataset.source and avoid some steps of data processing. You can switch .csv file to JSON using tools like dsv or PapaParse. As the example shown behind, in the data transmission of JavaScript, the two-dimensional data can be stored directly by two-dimensional array. Expect from the two-dimensional array, the dataset also supports using key-value which is also a common way. However, we don't support seriesLayoutBy in this format right now. dataset: [
  {
    // column by column key-value array is a normal format
    source: [
      { product: 'Matcha Latte', count: 823, score: 95.8 },
      { product: 'Milk Tea', count: 235, score: 81.4 },
      { product: 'Cheese Cocoa', count: 1042, score: 91.2 },
      { product: 'Walnut Brownie', count: 988, score: 76.9 }
    ]
  },
  {
    // row by row key-value
    source: {
      product: ['Matcha Latte', 'Milk Tea', 'Cheese Cocoa', 'Walnut Brownie'],
      count: [823, 235, 1042, 988],
      score: [95.8, 81.4, 91.2, 76.9]
    }
  }
];   How to Reference Several Datasets ECharts support to define several datasets at the same moment. Series can assign the one to reference by series.datasetIndex. For example: var option = {
  dataset: [
    {
      // 1st Dataset
      source: []
    },
    {
      // 2nd Dataset
      source: []
    },
    {
      // 3rd Dataset
      source: []
    }
  ],
  series: [
    {
      // Use 2nd dataset
      datasetIndex: 1
    },
    {
      // Use 1st dataset
      datasetIndex: 0
    }
  ]
};   series.data in ECharts 3 ECharts 4 still supports the data declaration way in ECharts 3. If the series has already declared the series.data, then use series.data but not dataset. option = {
  xAxis: {
    type: 'category',
    data: ['Matcha Latte', 'Milk Tea', 'Cheese Cocoa', 'Walnut Brownie']
  },
  yAxis: {},
  series: [
    {
      type: 'bar',
      name: '2015',
      data: [89.3, 92.1, 94.4, 85.4]
    },
    {
      type: 'bar',
      name: '2016',
      data: [95.8, 89.4, 91.2, 76.9]
    },
    {
      type: 'bar',
      name: '2017',
      data: [97.7, 83.1, 92.5, 78.1]
    }
  ]
};   In fact, series.data is an important setting method which will always exist. Some special non-table format chart like treemap, graph and lines still cannot be edit in dataset, you still need to use series.data. In another way, for render huge amount of data (over a million), you need to use appendData which is not supported by dataset. Others The following charts now support dataset:
line, bar, pie, scatter, effectScatter, parallel, candlestick, map, funnel, custom.
ECharts will support more charts in the future. In the end, here is an example of several charts shared one dataset with linkage interaction.

---

## Data Transform

**URL:** https://echarts.apache.org/handbook/en/concepts/data-transform/

**Contents:**
- Data Transform
- Get Started to Data Transform
- Advanced Usage
- Filter Transform
- Sort Transform
- Use External Transforms

Data Transform Data transform has been supported since Apache EChartsTM 5. In echarts, the term data transform refers to generating new data from user provided source data using transform functions. This feature enables users to process data in a declarative way and provides users several common "transform functions" to make such tasks work "out-of-the-box". (For consistency, we use the noun form "transform" rather than "transformation.") The abstract formula of a data transform is: outData = f(inputData), where the transform function f can be filter, sort, regression, boxplot, cluster, aggregate and so on.
With the help of these transform functions, users can implement features like: Partition data into multiple series. Compute statistics and visualize the results. Adapt visualization algorithms to the data and display the results. Sort data. Remove or choose certain kind of empty or special datums. ... Get Started to Data Transform In echarts, data transform is implemented based on the concept of dataset.You can specify a dataset.transform within a dataset instance to indicate that the dataset should be generated using the defined transform. For example: var option = {
  dataset: [
    {
      // This dataset is on `datasetIndex: 0`.
      source: [
        ['Product', 'Sales', 'Price', 'Year'],
        ['Cake', 123, 32, 2011],
        ['Cereal', 231, 14, 2011],
        ['Tofu', 235, 5, 2011],
        ['Dumpling', 341, 25, 2011],
        ['Biscuit', 122, 29, 2011],
        ['Cake', 143, 30, 2012],
        ['Cereal', 201, 19, 2012],
        ['Tofu', 255, 7, 2012],
        ['Dumpling', 241, 27, 2012],
        ['Biscuit', 102, 34, 2012],
        ['Cake', 153, 28, 2013],
        ['Cereal', 181, 21, 2013],
        ['Tofu', 395, 4, 2013],
        ['Dumpling', 281, 31, 2013],
        ['Biscuit', 92, 39, 2013],
        ['Cake', 223, 29, 2014],
        ['Cereal', 211, 17, 2014],
        ['Tofu', 345, 3, 2014],
        ['Dumpling', 211, 35, 2014],
        ['Biscuit', 72, 24, 2014]
      ]
      // id: 'a'
    },
    {
      // This dataset is on `datasetIndex: 1`.
      // A `transform` is configured to indicate that the
      // final data of this dataset is transformed via this
      // transform function.
      transform: {
        type: 'filter',
        config: { dimension: 'Year', value: 2011 }
      }
      // There can be optional properties `fromDatasetIndex` or `fromDatasetId`
      // to indicate that where is the input data of the transform from.
      // For example, `fromDatasetIndex: 0` specify the input data is from
      // the dataset on `datasetIndex: 0`, or `fromDatasetId: 'a'` specify the
      // input data is from the dataset having `id: 'a'`.
      // [DEFAULT_RULE]
      // If both `fromDatasetIndex` and `fromDatasetId` are omitted,
      // `fromDatasetIndex: 0` are used by default.
    },
    {
      // This dataset is on `datasetIndex: 2`.
      // Similarly, if neither `fromDatasetIndex` nor `fromDatasetId` is
      // specified, `fromDatasetIndex: 0` is used by default
      transform: {
        // The "filter" transform filters and gets data items only match
        // the given condition in property `config`.
        type: 'filter',
        // Transforms has a property `config`. In this "filter" transform,
        // the `config` specify the condition that each result data item
        // should be satisfied. In this case, this transform get all of
        // the data items that the value on dimension "Year" equals to 2012.
        config: { dimension: 'Year', value: 2012 }
      }
    },
    {
      // This dataset is on `datasetIndex: 3`
      transform: {
        type: 'filter',
        config: { dimension: 'Year', value: 2013 }
      }
    }
  ],
  series: [
    {
      type: 'pie',
      radius: 50,
      center: ['25%', '50%'],
      // In this case, each "pie" series reference to a dataset that has
      // the result of its "filter" transform.
      datasetIndex: 1
    },
    {
      type: 'pie',
      radius: 50,
      center: ['50%', '50%'],
      datasetIndex: 2
    },
    {
      type: 'pie',
      radius: 50,
      center: ['75%', '50%'],
      datasetIndex: 3
    }
  ]
}; live   Let's summarize the key points of using data transform: Generate new data from existing declared data via the declaration of transform, fromDatasetIndex/fromDatasetId in some blank dataset. Series references these datasets to show the result. Advanced Usage Piped Transform There is a syntactic sugar that pipe transforms like: option = {
  dataset: [
    {
      source: [] // The original data
    },
    {
      // Declare transforms in an array to pipe multiple transforms,
      // which makes them execute one by one and take the output of
      // the previous transform as the input of the next transform.
      transform: [
        {
          type: 'filter',
          config: { dimension: 'Product', value: 'Tofu' }
        },
        {
          type: 'sort',
          config: { dimension: 'Year', order: 'desc' }
        }
      ]
    }
  ],
  series: {
    type: 'pie',
    // Display the result of the piped transform.
    datasetIndex: 1
  }
};   Note: theoretically any type of transform is able to have multiple input data and multiple output data. But when a transform is piped, it is only able to take one input (except it is the first transform of the pipe) and product one output (except it is the last transform of the pipe). Output Multiple Data In most cases, transform functions only need to produce one data. But there is indeed scenarios that a transform function needs to produce multiple data, each of whom might be used by different series. For example, in the built-in boxplot transform, besides boxplot data produced, the outlier data are also produced, which can be used in a scatter series. See the example. We use prop dataset.fromTransformResult to satisfy this requirement. For example: option = {
  dataset: [
    {
      // Original source data.
      source: []
    },
    {
      transform: {
        type: 'boxplot'
      }
      // After this "boxplot transform" two result data generated:
      // result[0]: The boxplot data
      // result[1]: The outlier data
      // By default, when series or other dataset reference this dataset,
      // only result[0] can be visited.
      // If we need to visit result[1], we have to use another dataset
      // as follows:
    },
    {
      // This extra dataset references the dataset above, and retrieves
      // the result[1] as its own data. Thus series or other dataset can
      // reference this dataset to get the data from result[1].
      fromDatasetIndex: 1,
      fromTransformResult: 1
    }
  ],
  xAxis: {
    type: 'category'
  },
  yAxis: {},
  series: [
    {
      name: 'boxplot',
      type: 'boxplot',
      // Reference the data from result[0].
      datasetIndex: 1
    },
    {
      name: 'outlier',
      type: 'scatter',
      // Reference the data from result[1].
      datasetIndex: 2
    }
  ]
};   What more, dataset.fromTransformResult and dataset.transform can both appear in one dataset, which means that the input of the transform is from retrieved from the upstream result specified by fromTransformResult. For example: {
  fromDatasetIndex: 1,
  fromTransformResult: 1,
  transform: {
    type: 'sort',
    config: { dimension: 2, order: 'desc' }
  }
}   Debug in Develop Environment When using data transform, we might run into the trouble that the final chart do not display correctly but we do not know where the config is wrong. There is a property transform.print might help in such case. (transform.print is only available in dev environment). option = {
  dataset: [
    {
      source: []
    },
    {
      transform: {
        type: 'filter',
        config: {},
        // The result of this transform will be printed
        // in dev tool via `console.log`.
        print: true
      }
    }
  ]
};   Filter Transform Transform type "filter" is a built-in transform that provide data filter according to specified conditions. The basic option is like: option = {
  dataset: [
    {
      source: [
        ['Product', 'Sales', 'Price', 'Year'],
        ['Cake', 123, 32, 2011],
        ['Latte', 231, 14, 2011],
        ['Tofu', 235, 5, 2011],
        ['Milk Tee', 341, 25, 2011],
        ['Porridge', 122, 29, 2011],
        ['Cake', 143, 30, 2012],
        ['Latte', 201, 19, 2012],
        ['Tofu', 255, 7, 2012],
        ['Milk Tee', 241, 27, 2012],
        ['Porridge', 102, 34, 2012],
        ['Cake', 153, 28, 2013],
        ['Latte', 181, 21, 2013],
        ['Tofu', 395, 4, 2013],
        ['Milk Tee', 281, 31, 2013],
        ['Porridge', 92, 39, 2013],
        ['Cake', 223, 29, 2014],
        ['Latte', 211, 17, 2014],
        ['Tofu', 345, 3, 2014],
        ['Milk Tee', 211, 35, 2014],
        ['Porridge', 72, 24, 2014]
      ]
    },
    {
      transform: {
        type: 'filter',
        config: { dimension: 'Year', '=': 2011 }
        // The config is the "condition" of this filter.
        // This transform traverse the source data and
        // and retrieve all the items that the "Year"
        // is `2011`.
      }
    }
  ],
  series: {
    type: 'pie',
    datasetIndex: 1
  }
}; live   This is another example of filter transform:  About dimension: The config.dimension can be: Dimension name declared in dataset, like config: { dimension: 'Year', '=': 2011 }. Dimension name declaration is not mandatory. Dimension index (start from 0), like config: { dimension: 3, '=': 2011 }. About relational operator: The relational operator can be:
>(gt), >=(gte), <(lt), <=(lte), =(eq), !=(ne, <>), reg. (The name in the parentheses are aliases). They follows the common semantics.
Besides the common number comparison, there is some extra features: Multiple operators are able to appear in one {} item like { dimension: 'Price', '>=': 20, '<': 30 }, which means logical "and" (Price >= 20 and Price < 30). The data value can be "numeric string". Numeric string is a string that can be converted to number. Like ' 123 '. White spaces and line breaks will be auto trimmed in the conversion. If we need to compare "JS Date instance" or date string (like '2012-05-12'), we need to specify parser: 'time' manually, like config: { dimension: 3, lt: '2012-05-12', parser: 'time' }. Pure string comparison is supported but can only be used in =, !=. >, >=, <, <= do not support pure string comparison (the "right value" of the four operators can not be a "string"). The operator reg can be used to make regular expression test. Like using { dimension: 'Name', reg: /\s+Müller\s*$/ } to select all data items that the "Name" dimension contains family name Müller. About logical relationship: Sometimes we also need to express logical relationship ( and / or / not ): option = {
  dataset: [
    {
      source: [
        // ...
      ]
    },
    {
      transform: {
        type: 'filter',
        config: {
          // Use operator "and".
          // Similarly, we can also use "or", "not" in the same place.
          // But "not" should be followed with a {...} rather than `[...]`.
          and: [
            { dimension: 'Year', '=': 2011 },
            { dimension: 'Price', '>=': 20, '<': 30 }
          ]
        }
        // The condition is "Year" is 2011 and "Price" is greater
        // or equal to 20 but less than 30.
      }
    }
  ],
  series: {
    type: 'pie',
    datasetIndex: 1
  }
};   and/or/not can be nested like: transform: {
  type: 'filter',
  config: {
    or: [{
      and: [{
        dimension: 'Price', '>=': 10, '<': 20
      }, {
        dimension: 'Sales', '<': 100
      }, {
        not: { dimension: 'Product', '=': 'Tofu' }
      }]
    }, {
      and: [{
        dimension: 'Price', '>=': 10, '<': 20
      }, {
        dimension: 'Sales', '<': 100
      }, {
        not: { dimension: 'Product', '=': 'Cake' }
      }]
    }]
  }
}   About parser: Some "parser" can be specified when make value comparison. At present only supported: parser: 'time': Parse the value to date time before comparing. The parser rule is the same as echarts.time.parse, where JS Date instance, timestamp number (in millisecond) and time string (like '2012-05-12 03:11:22') are supported to be parse to timestamp number, while other value will be parsed to NaN. parser: 'trim': Trim the string before making comparison. For non-string, return the original value. parser: 'number': Force to convert the value to number before making comparison. If not possible to be converted to a meaningful number, converted to NaN. In most cases it is not necessary, because by default the value will be auto converted to number if possible before making comparison. But the default conversion is strict while this parser provide a loose strategy. If we meet the case that number string with unit suffix (like '33%', 12px), we should use parser: 'number' to convert them to number before making comparison. This is an example to show the parser: 'time': option = {
  dataset: [
    {
      source: [
        ['Product', 'Sales', 'Price', 'Date'],
        ['Milk Tee', 311, 21, '2012-05-12'],
        ['Cake', 135, 28, '2012-05-22'],
        ['Latte', 262, 36, '2012-06-02'],
        ['Milk Tee', 359, 21, '2012-06-22'],
        ['Cake', 121, 28, '2012-07-02'],
        ['Latte', 271, 36, '2012-06-22']
        // ...
      ]
    },
    {
      transform: {
        type: 'filter',
        config: {
          dimension: 'Date',
          '>=': '2012-05',
          '<': '2012-06',
          parser: 'time'
        }
      }
    }
  ]
};   Formally definition: Finally, we give the formally definition of the filter transform config here: type FilterTransform = {
  type: 'filter';
  config: ConditionalExpressionOption;
};
type ConditionalExpressionOption =
  | true
  | false
  | RelationalExpressionOption
  | LogicalExpressionOption;
type RelationalExpressionOption = {
  dimension: DimensionName | DimensionIndex;
  parser?: 'time' | 'trim' | 'number';
  lt?: DataValue; // less than
  lte?: DataValue; // less than or equal
  gt?: DataValue; // greater than
  gte?: DataValue; // greater than or equal
  eq?: DataValue; // equal
  ne?: DataValue; // not equal
  '<'?: DataValue; // lt
  '<='?: DataValue; // lte
  '>'?: DataValue; // gt
  '>='?: DataValue; // gte
  '='?: DataValue; // eq
  '!='?: DataValue; // ne
  '<>'?: DataValue; // ne (SQL style)
  reg?: RegExp | string; // RegExp
};
type LogicalExpressionOption = {
  and?: ConditionalExpressionOption[];
  or?: ConditionalExpressionOption[];
  not?: ConditionalExpressionOption;
};
type DataValue = string | number | Date;
type DimensionName = string;
type DimensionIndex = number;   Note that when using Minimal Bundle, if you need to use this built-in transform, besides the Dataset component, it's required to import the Transform component. import {
  DatasetComponent,
  TransformComponent
} from 'echarts/components';

echarts.use([
  DatasetComponent,
  TransformComponent
]);   Sort Transform Another built-in transform is "sort". option = {
  dataset: [
    {
      dimensions: ['name', 'age', 'profession', 'score', 'date'],
      source: [
        [' Hannah Krause ', 41, 'Engineer', 314, '2011-02-12'],
        ['Zhao Qian ', 20, 'Teacher', 351, '2011-03-01'],
        [' Jasmin Krause ', 52, 'Musician', 287, '2011-02-14'],
        ['Li Lei', 37, 'Teacher', 219, '2011-02-18'],
        [' Karle Neumann ', 25, 'Engineer', 253, '2011-04-02'],
        [' Adrian Groß', 19, 'Teacher', null, '2011-01-16'],
        ['Mia Neumann', 71, 'Engineer', 165, '2011-03-19'],
        [' Böhm Fuchs', 36, 'Musician', 318, '2011-02-24'],
        ['Han Meimei ', 67, 'Engineer', 366, '2011-03-12']
      ]
    },
    {
      transform: {
        type: 'sort',
        // Sort by score.
        config: { dimension: 'score', order: 'asc' }
      }
    }
  ],
  series: {
    type: 'bar',
    datasetIndex: 1
  }
  // ...
};    Some extra features about "sort transform": Order by multiple dimensions is supported. See examples below. The sort rule:
By default "numeric" (that is, number and numeric-string like ' 123 ') are able to sorted by numeric order. Otherwise "non-numeric-string" are also able to be ordered among themselves. This might help to the case like grouping data items with the same tag, especially when multiple dimensions participated in the sort (See example below). When "numeric" is compared with "non-numeric-string", or either of them is compared with other types of value, they are not comparable. So we call the latter one as "incomparable" and treat it as "min value" or "max value" according to the prop incomparable: 'min' | 'max'. This feature usually helps to decide whether to put the empty values (like null, undefined, NaN, '', '-') or other illegal values to the head or tail. parser: 'time' | 'trim' | 'number' can be used, the same as "filter transform".
If intending to sort time values (JS Date instance or time string like '2012-03-12 11:13:54'), parser: 'time' should be specified. Like config: { dimension: 'date', order: 'desc', parser: 'time' } If intending to sort values with unit suffix (like '33%', '16px'), need to use parser: 'number'. See an example of multiple order: option = {
  dataset: [
    {
      dimensions: ['name', 'age', 'profession', 'score', 'date'],
      source: [
        [' Hannah Krause ', 41, 'Engineer', 314, '2011-02-12'],
        ['Zhao Qian ', 20, 'Teacher', 351, '2011-03-01'],
        [' Jasmin Krause ', 52, 'Musician', 287, '2011-02-14'],
        ['Li Lei', 37, 'Teacher', 219, '2011-02-18'],
        [' Karle Neumann ', 25, 'Engineer', 253, '2011-04-02'],
        [' Adrian Groß', 19, 'Teacher', null, '2011-01-16'],
        ['Mia Neumann', 71, 'Engineer', 165, '2011-03-19'],
        [' Böhm Fuchs', 36, 'Musician', 318, '2011-02-24'],
        ['Han Meimei ', 67, 'Engineer', 366, '2011-03-12']
      ]
    },
    {
      transform: {
        type: 'sort',
        config: [
          // Sort by the two dimensions.
          { dimension: 'profession', order: 'desc' },
          { dimension: 'score', order: 'desc' }
        ]
      }
    }
  ],
  series: {
    type: 'bar',
    datasetIndex: 1
  }
  // ...
};    Finally, we give the formally definition of the sort transform config here: type SortTransform = {
  type: 'sort';
  config: OrderExpression | OrderExpression[];
};
type OrderExpression = {
  dimension: DimensionName | DimensionIndex;
  order: 'asc' | 'desc';
  incomparable?: 'min' | 'max';
  parser?: 'time' | 'trim' | 'number';
};
type DimensionName = string;
type DimensionIndex = number;   Note that when using Minimal Bundle, if you need to use this built-in transform, besides the Dataset component, it's required to import the Transform component. import {
  DatasetComponent,
  TransformComponent
} from 'echarts/components';

echarts.use([
  DatasetComponent,
  TransformComponent
]);   Use External Transforms Besides built-in transforms (like 'filter', 'sort'), we can also use external transforms to provide more powerful functionalities. Here we use a third-party library ecStat as an example: This case show how to make a regression line via ecStat: // Register the external transform at first.
echarts.registerTransform(ecStatTransform(ecStat).regression);   option = {
  dataset: [
    {
      source: rawData
    },
    {
      transform: {
        // Reference the registered external transform.
        // Note that external transform has a namespace (like 'ecStat:xxx'
        // has namespace 'ecStat').
        // built-in transform (like 'filter', 'sort') does not have a namespace.
        type: 'ecStat:regression',
        config: {
          // Parameters needed by the external transform.
          method: 'exponential'
        }
      }
    }
  ],
  xAxis: { type: 'category' },
  yAxis: {},
  series: [
    {
      name: 'scatter',
      type: 'scatter',
      datasetIndex: 0
    },
    {
      name: 'regression',
      type: 'line',
      symbol: 'none',
      datasetIndex: 1
    }
  ]
};   Examples with echarts-stat: Aggregate Bar histogram Scatter clustering Scatter linear regression Scatter exponential regression Scatter logarithmic regression Scatter polynomial regression

---

## Event and Action

**URL:** https://echarts.apache.org/handbook/en/concepts/event/

**Contents:**
- Event and Action
- Handling the Mouse Events
- Event of Component Interaction
- Writing Code to Trigger Component Action Manually
- Listen to Events on the Blank Area

Event and Action Users can trigger corresponding events by their operation. The developer can handle the callback function by listening to these events, such as jump to a new website, pop-up a dialog box, or drill down the data. The name of the event and the DOM event is both lowercase string. Here is an example of binding listening to click event. myChart.on('click', function(params) {
  // Print name in console
  console.log(params.name);
});   There are two kinds of event in ECharts, one happened when the user clicks the mouse or hover the elements in charts, the other happened while the user triggered some interactive actions. Such as 'legendselectchanged' triggered while changing the legend selected (please notice that legendselected won't be triggered in this situation), 'datazoom' triggered while zooming the data area. Handling the Mouse Events ECharts support general mouse events: 'click', 'dblclick', 'mousedown', 'mousemove', 'mouseup', 'mouseover', 'mouseout', 'globalout', 'contextmenu'. This is an example of opening the search result page after clicking the bar chart. // Init the ECharts base on DOM
var myChart = echarts.init(document.getElementById('main'));

// Config
var option = {
  xAxis: {
    data: [
      'Shirt',
      'Wool sweater',
      'Chiffon shirt',
      'Pants',
      'High-heeled shoes',
      'socks'
    ]
  },
  yAxis: {},
  series: [
    {
      name: 'Sales',
      type: 'bar',
      data: [5, 20, 36, 10, 10, 20]
    }
  ]
};
// Use the option and data to display the chart
myChart.setOption(option);
// Click and jump to Baidu search website
myChart.on('click', function(params) {
  window.open(
    'https://www.google.com/search?q=' + encodeURIComponent(params.name)
  );
});   All mouse events included params which contained the data of the object. Format: type EventParams = {
  // The component name clicked,
  // component type, could be 'series'、'markLine'、'markPoint'、'timeLine', etc..
  componentType: string,
  // series type, could be 'line'、'bar'、'pie', etc.. Works when componentType is 'series'.
  seriesType: string,
  // the index in option.series. Works when componentType is 'series'.
  seriesIndex: number,
  // series name, works when componentType is 'series'.
  seriesName: string,
  // name of data (categories).
  name: string,
  // the index in 'data' array.
  dataIndex: number,
  // incoming raw data item
  data: Object,
  // charts like 'sankey' and 'graph' included nodeData and edgeData as the same time.
  // dataType can be 'node' or 'edge', indicates whether the current click is on node or edge.
  // most of charts have one kind of data, the dataType is meaningless
  dataType: string,
  // incoming data value
  value: number | Array,
  // color of the shape, works when componentType is 'series'.
  color: string
};   Identify where the mouse clicked. myChart.on('click', function(params) {
  if (params.componentType === 'markPoint') {
    // Clicked on the markPoint
    if (params.seriesIndex === 5) {
      // clicked on the markPoint of the series with index = 5
    }
  } else if (params.componentType === 'series') {
    if (params.seriesType === 'graph') {
      if (params.dataType === 'edge') {
        // clicked at the edge of graph.
      } else {
        // clicked at the node of graph.
      }
    }
  }
});   Use query to trigger callback of the specified component: chart.on(eventName, query, handler);   query can be string or Object. If it is string, the format can be mainType or mainType.subType, such as: chart.on('click', 'series', function () {...});
chart.on('click', 'series.line', function () {...});
chart.on('click', 'dataZoom', function () {...});
chart.on('click', 'xAxis.category', function () {...});   If it is Object, query can include more than one attribute: {
  ${mainType}Index: number // component index
  ${mainType}Name: string // component name
  ${mainType}Id: string // component id
  dataIndex: number // data item index
  name: string // data item name
  dataType: string // date item type, such as 'node', 'edge'
  element: string // name of element in custom series.
}   Such as: chart.setOption({
  // ...
  series: [
    {
      name: 'uuu'
      // ...
    }
  ]
});
chart.on('mouseover', { seriesName: 'uuu' }, function() {
  // when elements in series named 'uuu' triggered 'mouseover'
});   For example: chart.setOption({
  // ...
  series: [
    {
      // ...
    },
    {
      // ...
      data: [
        { name: 'xx', value: 121 },
        { name: 'yy', value: 33 }
      ]
    }
  ]
});
chart.on('mouseover', { seriesIndex: 1, name: 'xx' }, function() {
  // when data named 'xx' in series index 1 triggered 'mouseover'.
});   For example: chart.setOption({
  // ...
  series: [
    {
      type: 'graph',
      nodes: [
        { name: 'a', value: 10 },
        { name: 'b', value: 20 }
      ],
      edges: [{ source: 0, target: 1 }]
    }
  ]
});
chart.on('click', { dataType: 'node' }, function() {
  // call this method while the node of graph was clicked.
});
chart.on('click', { dataType: 'edge' }, function() {
  // call this method while the edge of graph was clicked.
});   For example: chart.setOption({
  // ...
  series: {
    // ...
    type: 'custom',
    renderItem: function(params, api) {
      return {
        type: 'group',
        children: [
          {
            type: 'circle',
            name: 'my_el'
            // ...
          },
          {
            // ...
          }
        ]
      };
    },
    data: [[12, 33]]
  }
});
chart.on('mouseup', { element: 'my_el' }, function() {
  // when data named 'my_el' triggered 'mouseup'.
});   You can display a popup, update the charts using the query result from your database by the data name or series name in the callback function. Here is an example: myChart.on('click', function(parmas) {
  $.get('detail?q=' + params.name, function(detail) {
    myChart.setOption({
      series: [
        {
          name: 'pie',
          // using pie chart to show the data distribution in one column.
          data: [detail.data]
        }
      ]
    });
  });
});   Event of Component Interaction All Component Interaction in ECharts will trigger a corresponding event. Normal events and parameters are listed in the events document. Here is an example of listening to legend event: // Show/hide the legend only trigger legendselectchanged event
myChart.on('legendselectchanged', function(params) {
  // State if legend is selected.
  var isSelected = params.selected[params.name];
  // print in the console.
  console.log(
    (isSelected ? 'Selected' : 'Not Selected') + 'legend' + params.name
  );
  // print for all legends.
  console.log(params.selected);
});   Writing Code to Trigger Component Action Manually You can trigger events such as 'legendselectchanged' not only by the user but also with code manually. It can be used to display the tooltip, select the legend. In ECharts myChart.dispatchAction({ type: '' }) is used to trigger the behavior. This manages all actions and can record the behaviors conveniently. Commonly used behavior and corresponding parameters are listed in action. The following example shows how to highlight each sector one by one in the pie chart using dispatchAction. option = {
  tooltip: {
    trigger: 'item',
    formatter: '{a} <br/>{b} : {c} ({d}%)'
  },
  legend: {
    orient: 'vertical',
    left: 'left',
    data: [
      'Direct Access',
      'Email Marketing',
      'Affiliate Ads',
      'Video Ads',
      'Search Engines'
    ]
  },
  series: [
    {
      name: 'Access Source',
      type: 'pie',
      radius: '55%',
      center: ['50%', '60%'],
      data: [
        { value: 335, name: 'Direct Access' },
        { value: 310, name: 'Email Marketing' },
        { value: 234, name: 'Affiliate Ads' },
        { value: 135, name: 'Video Ads' },
        { value: 1548, name: 'Search Engines' }
      ],
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.5)'
        }
      }
    }
  ]
};

let currentIndex = -1;

setInterval(function() {
  var dataLen = option.series[0].data.length;
  myChart.dispatchAction({
    type: 'downplay',
    seriesIndex: 0,
    dataIndex: currentIndex
  });
  currentIndex = (currentIndex + 1) % dataLen;
  myChart.dispatchAction({
    type: 'highlight',
    seriesIndex: 0,
    dataIndex: currentIndex
  });
  myChart.dispatchAction({
    type: 'showTip',
    seriesIndex: 0,
    dataIndex: currentIndex
  });
}, 1000); live   Listen to Events on the Blank Area Sometimes developers need to listen to the events that are triggered from the blank of the canvas. For example, need to reset the chart when users click on the blank area. Before we talk about this feature, we need to clarify two kinds of events: zrender events and echarts events. myChart.getZr().on('click', function(event) {
  // This listener is listening to a `zrender event`.
});
myChart.on('click', function(event) {
  // This listener is listening to a `echarts event`.
});   zrender events are different from echarts events. The former one are triggered when mouse/pointer is at everywhere, while the latter one can only be triggered when mouse/pointer is at the graphic elements. In fact, echarts events are implemented based on zrender events, that is, when a zrender events is triggered at a graphic element, echarts will trigger a echarts event. Having zrender events, we can implement listen to events from the blank as follows: myChart.getZr().on('click', function(event) {
  // No "target" means that mouse/pointer is not on
  // any of the graphic elements, which is "blank".
  if (!event.target) {
    // Click on blank. Do something.
  }
});  

---

## Legend

**URL:** https://echarts.apache.org/handbook/en/concepts/legend/

**Contents:**
- Legend
- Layout
- Style
- Interactive
- Tips

Legend Legends are used to annotate the content in the chart using different colors, shapes and texts to indicate different categories. By clicking the legends, the user can show or hide the corresponding categories. Legend is one of the key to understand the chart. Layout Legend is always placed at the upper right corner of the chart. All legends in the same page need to be consistent, align horizontally or vertically by considering the layout of the overall chart space. When the chart has little vertical space or the content area is crowded, it is also a good choice to put the legend on the bottom of the chart. Here are some layouts of legend: option = {
  legend: {
    // Try 'horizontal'
    orient: 'vertical',
    right: 10,
    top: 'center'
  },
  dataset: {
    source: [
      ['product', '2015', '2016', '2017'],
      ['Matcha Latte', 43.3, 85.8, 93.7],
      ['Milk Tea', 83.1, 73.4, 55.1],
      ['Cheese Cocoa', 86.4, 65.2, 82.5],
      ['Walnut Brownie', 72.4, 53.9, 39.1]
    ]
  },
  xAxis: { type: 'category' },
  yAxis: {},
  series: [{ type: 'bar' }, { type: 'bar' }, { type: 'bar' }]
}; live   Use scrollable control if there are many legends. option = {
  legend: {
    type: 'scroll',
    orient: 'vertical',
    right: 10,
    top: 20,
    bottom: 20,
    data: ['Legend A', 'Legend B', 'Legend C' /* ... */, , 'Legend x']
    // ...
  }
  // ...
};   Style For dark color background, use a light color for the background layer and text while changing the background to translucent. option = {
  legend: {
    data: ['Legend A', 'Legend B', 'Legend C'],
    backgroundColor: '#ccc',
    textStyle: {
      color: '#ccc'
      // ...
    }
    // ...
  }
  // ...
};   The color of legend has many ways to design. For different charts, the legend style can be different.  option = {
  legend: {
    data: ['Legend A', 'Legend B', 'Legend C'],
    icon: 'rect'
    // ...
  }
  // ...
};   Interactive Depend on the environmental demand, the legend can support interactive operation. Click the legend to show or hide corresponding categories: option = {
  legend: {
    data: ['Legend A', 'Legend B', 'Legend C'],
    selected: {
      'Legend A': true,
      'Legend B': true,
      'Legend C': false
    }
    // ...
  }
  // ...
};   Tips The legend should be used according to the situation. Some dual-axis charts include multiple chart types. Different kinds of legend stypes should be distinguished. option = {
  legend: {
    data: [
      {
        name: 'Legend A',
        icon: 'rect'
      },
      {
        name: 'Legend B',
        icon: 'circle'
      },
      {
        name: 'Legend C',
        icon: 'pin'
      }
    ]
    //  ...
  },
  series: [
    {
      name: 'Legend A'
      //  ...
    },
    {
      name: 'Legend B'
      //  ...
    },
    {
      name: 'Legend C'
      //  ...
    }
  ]
  //  ...
};   While there is only one kind of data in the chart, use the chart title rather than the legend to explain it.

---

## Overview of Style Customization

**URL:** https://echarts.apache.org/handbook/en/concepts/style/

**Contents:**
- Overview of Style Customization
- Theme
- Color Palette
- Customize Style Explicitly
- Style of Emphasis State
- Visual Encoding by visualMap Component

Overview of Style Customization This article provides an overview of the different approaches about Apache EChartsTM style customization. For example, how to config the color, size, shadow of the graphic elements and labels. The term "style" may not follow the convention of data visualization, but we use it in this article because it is popular and easy to understand. These approaches below will be introduced. The functionalities of them might be overlapped, but they are suitable for different scenarios. Theme Color Palette Customize style explicitly (itemStyle, lineStyle, areaStyle, label, ...) Visual encoding (visualMap component) Theme Setting a theme is the simplest way to change the color style. For example, in Examples page, we can switch to dark mode and see the result of a different theme. In our project, we can switch to dark theme like: var chart = echarts.init(dom, 'dark');   Other themes are not included by default, and need to load them ourselves if we want to use them. Themes can be visited and downloaded in the theme builder. Theme can also be created or edited in it. The downloaded theme can be used as follows: If a theme is downloaded as a JSON file, we should register it by ourselves, for example: // Assume the theme name is "vintage".
fetch('theme/vintage.json')
  .then(r => r.json())
  .then(theme => {
    echarts.registerTheme('vintage', theme);
    var chart = echarts.init(dom, 'vintage');
  })   If a theme is downloaded as a JS file, it will auto register itself: // Import the `vintage.js` file in HTML, then:
var chart = echarts.init(dom, 'vintage');
// ...   Color Palette Color palette can be given in option. They provide a group of colors, which will be auto picked by series and data. We can give a global palette, or exclusive pallette for certain series. option = {
  // Global palette:
  color: [
    '#c23531',
    '#2f4554',
    '#61a0a8',
    '#d48265',
    '#91c7ae',
    '#749f83',
    '#ca8622',
    '#bda29a',
    '#6e7074',
    '#546570',
    '#c4ccd3'
  ],

  series: [
    {
      type: 'bar',
      // A palette only work for the series:
      color: [
        '#dd6b66',
        '#759aa0',
        '#e69d87',
        '#8dc1a9',
        '#ea7e53',
        '#eedd78',
        '#73a373',
        '#73b9bc',
        '#7289ab',
        '#91ca8c',
        '#f49f42'
      ]
      // ...
    },
    {
      type: 'pie',
      // A palette only work for the series:
      color: [
        '#37A2DA',
        '#32C5E9',
        '#67E0E3',
        '#9FE6B8',
        '#FFDB5C',
        '#ff9f7f',
        '#fb7293',
        '#E062AE',
        '#E690D1',
        '#e7bcf3',
        '#9d96f5',
        '#8378EA',
        '#96BFFF'
      ]
      // ...
    }
  ]
};   Customize Style Explicitly It is a common way to set style explicitly. Throughout ECharts option, style related options can be set in various place, including itemStyle, lineStyle, areaStyle, label, etc. Generally speaking, all of the built-in components and series follow the naming convention like itemStyle, lineStyle, areaStyle, label etc, although they may occur in different place according to different series or components. In the following code we add shadow, gradient to bubble chart. var data = [
  [
    [28604, 77, 17096869, 'Australia', 1990],
    [31163, 77.4, 27662440, 'Canada', 1990],
    [1516, 68, 1154605773, 'China', 1990],
    [13670, 74.7, 10582082, 'Cuba', 1990],
    [28599, 75, 4986705, 'Finland', 1990],
    [29476, 77.1, 56943299, 'France', 1990],
    [31476, 75.4, 78958237, 'Germany', 1990],
    [28666, 78.1, 254830, 'Iceland', 1990],
    [1777, 57.7, 870601776, 'India', 1990],
    [29550, 79.1, 122249285, 'Japan', 1990],
    [2076, 67.9, 20194354, 'North Korea', 1990],
    [12087, 72, 42972254, 'South Korea', 1990],
    [24021, 75.4, 3397534, 'New Zealand', 1990],
    [43296, 76.8, 4240375, 'Norway', 1990],
    [10088, 70.8, 38195258, 'Poland', 1990],
    [19349, 69.6, 147568552, 'Russia', 1990],
    [10670, 67.3, 53994605, 'Turkey', 1990],
    [26424, 75.7, 57110117, 'United Kingdom', 1990],
    [37062, 75.4, 252847810, 'United States', 1990]
  ],
  [
    [44056, 81.8, 23968973, 'Australia', 2015],
    [43294, 81.7, 35939927, 'Canada', 2015],
    [13334, 76.9, 1376048943, 'China', 2015],
    [21291, 78.5, 11389562, 'Cuba', 2015],
    [38923, 80.8, 5503457, 'Finland', 2015],
    [37599, 81.9, 64395345, 'France', 2015],
    [44053, 81.1, 80688545, 'Germany', 2015],
    [42182, 82.8, 329425, 'Iceland', 2015],
    [5903, 66.8, 1311050527, 'India', 2015],
    [36162, 83.5, 126573481, 'Japan', 2015],
    [1390, 71.4, 25155317, 'North Korea', 2015],
    [34644, 80.7, 50293439, 'South Korea', 2015],
    [34186, 80.6, 4528526, 'New Zealand', 2015],
    [64304, 81.6, 5210967, 'Norway', 2015],
    [24787, 77.3, 38611794, 'Poland', 2015],
    [23038, 73.13, 143456918, 'Russia', 2015],
    [19360, 76.5, 78665830, 'Turkey', 2015],
    [38225, 81.4, 64715810, 'United Kingdom', 2015],
    [53354, 79.1, 321773631, 'United States', 2015]
  ]
];

option = {
  backgroundColor: {
    type: 'radial',
    x: 0.3,
    y: 0.3,
    r: 0.8,
    colorStops: [
      {
        offset: 0,
        color: '#f7f8fa'
      },
      {
        offset: 1,
        color: '#cdd0d5'
      }
    ]
  },
  grid: {
    left: 10,
    containLabel: true,
    bottom: 10,
    top: 10,
    right: 30
  },
  xAxis: {
    splitLine: {
      show: false
    }
  },
  yAxis: {
    splitLine: {
      show: false
    },
    scale: true
  },
  series: [
    {
      name: '1990',
      data: data[0],
      type: 'scatter',
      symbolSize: function(data) {
        return Math.sqrt(data[2]) / 5e2;
      },
      emphasis: {
        focus: 'series',
        label: {
          show: true,
          formatter: function(param) {
            return param.data[3];
          },
          position: 'top'
        }
      },
      itemStyle: {
        shadowBlur: 10,
        shadowColor: 'rgba(120, 36, 50, 0.5)',
        shadowOffsetY: 5,
        color: {
          type: 'radial',
          x: 0.4,
          y: 0.3,
          r: 1,
          colorStops: [
            {
              offset: 0,
              color: 'rgb(251, 118, 123)'
            },
            {
              offset: 1,
              color: 'rgb(204, 46, 72)'
            }
          ]
        }
      }
    },
    {
      name: '2015',
      data: data[1],
      type: 'scatter',
      symbolSize: function(data) {
        return Math.sqrt(data[2]) / 5e2;
      },
      emphasis: {
        focus: 'series',
        label: {
          show: true,
          formatter: function(param) {
            return param.data[3];
          },
          position: 'top'
        }
      },
      itemStyle: {
        shadowBlur: 10,
        shadowColor: 'rgba(25, 100, 150, 0.5)',
        shadowOffsetY: 5,
        color: {
          type: 'radial',
          x: 0.4,
          y: 0.3,
          r: 1,
          colorStops: [
            {
              offset: 0,
              color: 'rgb(129, 227, 238)'
            },
            {
              offset: 1,
              color: 'rgb(25, 183, 207)'
            }
          ]
        }
      }
    }
  ]
}; live   Style of Emphasis State When mouse hovering a graphic elements, usually the emphasis style will be displayed. By default, the emphasis style is auto generated by the normal style. However they can be specified by emphasis property. The options in emphasis is the same as the ones for normal state, for example: option = {
  series: {
    type: 'scatter',

    // Styles for normal state.
    itemStyle: {
      // Color of the point.
      color: 'red'
    },
    label: {
      show: true,
      // Text of labels.
      formatter: 'This is a normal label.'
    },

    // Styles for emphasis state.
    emphasis: {
      itemStyle: {
        // Color in emphasis state.
        color: 'blue'
      },
      label: {
        show: true,
        // Text in emphasis.
        formatter: 'This is a emphasis label.'
      }
    }
  }
};   Notice: Before ECharts4, the emphasis style should be written like this: option = {
  series: {
    type: 'scatter',

    itemStyle: {
      // Styles for normal state.
      normal: {
        color: 'red'
      },
      // Styles for emphasis state.
      emphasis: {
        color: 'blue'
      }
    },

    label: {
      // Styles for normal state.
      normal: {
        show: true,
        formatter: 'This is a normal label.'
      },
      // Styles for emphasis state.
      emphasis: {
        show: true,
        formatter: 'This is a emphasis label.'
      }
    }
  }
};   The option format is still compatible, but not recommended. In fact, in most cases, users only set normal style, and use the default emphasis style. So since ECharts4, we support to write style without the "normal" term, which makes the option more simple and neat. Visual Encoding by visualMap Component visualMap component supports config the rule that mapping value to visual channel (color, size, ...). More details can be check in Visual Map of Data.

---

## Visual Map of Data

**URL:** https://echarts.apache.org/handbook/en/concepts/visual-map/

**Contents:**
- Visual Map of Data
- Data and Dimension
- The visualMap Component
- Continuous and Piecewise Visual Mapping Components
  - Continuous Visual Mapping
  - Piecewise Visual Mapping

Visual Map of Data Data visualization is a procedure of mapping data into visual elements. This procedure can also be called visual coding, and visual elements can also be called visual channels. Every type of charts in Apache EChartsTM has this built-in mapping procedure. For example, line chart map data into lines, bar chart map data into height. Some more complicated charts, like graph, themeRiver, and treemap have their own built-in mapping. Besides, ECharts provides visualMap component for general visual mapping. Visual elements allowed in visualMap component are: symbol, symbolSize color, opacity, colorAlpha, colorLightness, colorSaturation, colorHue Next, we are going to introduce how to use visualMap component. Data and Dimension Data are usually stored in series.data in ECharts. Depending on chart types, like list, tree, graph, and so on, the form of data may vary somehow. But they have one common feature, that they are a collection of data items. Every data item contains data value, and other information if needed. Every data value can be a single value (one dimension) or an array (multiple dimensions). For example, series.data is the most common form, which is a list, a common array: series: {
  data: [
    {
      // every item here is a dataItem
      value: 2323, // this is data value
      itemStyle: {}
    },
    1212, // it can also be a value of dataItem, which is a more common case
    2323, // every data value here is one dimension
    4343,
    3434
  ];
}   series: {
  data: [
    {
      // every item here is a dataItem
      value: [3434, 129, 'San Marino'], // this is data value
      itemStyle: {}
    },
    [1212, 5454, 'Vatican'], // it can also be a value of dataItem, which is a more common case
    [2323, 3223, 'Nauru'], // every data value here is three dimension
    [4343, 23, 'Tuvalu'] // If is scatter chart, usually map the first dimension to x axis,
    // the second dimension to y axis,
    // and the third dimension to symbolSize
  ];
}   Usually the first one or two dimensions are used for mapping. For example, map the first dimension to x axis, and the second dimension to y axis. If you want to represent more dimensions, visualMap is what you need. Most likely, scatter charts use radius to represent the third dimension. The visualMap Component visualMap component defines the mapping from which dimension of data to what visual elements. The following two types of visualMap components are supported, identified with visualMap.type. Its structure is defined as: option = {
  visualMap: [
    // can define multiple visualMap components at the same time
    {
      // the first visualMap component
      type: 'continuous' // defined as continuous visualMap
      // ...
    },
    {
      // the second visualMap component
      type: 'piecewise' // defined as discrete visualMap
      // ...
    }
  ]
  // ...
};   Continuous and Piecewise Visual Mapping Components The visual mapping component of ECharts is divided into continuous (visualMapContinuous) and piecewise (visualMapPiecewise). Continuous means that the data dimension for visual mapping is a continuous value, while piecewise means that the data is divided into multiple segments or discrete data. Continuous Visual Mapping Continuous type visual mapping can determine the range of visual mapping by specifying the maximum and minimum values. option = {
  visualMap: [
    {
      type: 'continuous',
      min: 0,
      max: 5000,
      dimension: 3, // the fourth dimension of series.data (i.e. value[3]) is mapped
      seriesIndex: 4, // The fourth series is mapped.
      inRange: {
        // The visual configuration in the selected range
        color: ['blue', '#121122', 'red'], // A list of colors that defines the graph color mapping
        // the minimum value of the data is mapped to 'blue', and
        // the maximum value is mapped to 'red', // the maximum value is mapped to 'red', // the maximum value is mapped to 'red'.
        // The rest is automatically calculated linearly.
        symbolSize: [30, 100] // Defines the mapping range for the graphic size.
        // The minimum value of the data is mapped to 30, // and the maximum value is mapped to 100.
        // The maximum value is mapped to 100.
        // The rest is calculated linearly automatically.
      },
      outOfRange: {
        // Check the out of range visual configuration
        symbolSize: [30, 100]
      }
    }
    // ...
  ]
};   where visualMap.inRange indicates the style used for data within the data mapping range; while visualMap.outOfRange specifies the style for data outside the mapping range. visualMap.dimension specifies which dimension of the data will be visually mapped. Piecewise Visual Mapping The piecewise visual mapping component has three modes. Continuous data average segmentation: based on visualMap-piecewise.splitNumber to automatically split the data into pieces equally. Continuous data custom segmentation: define the range of each piece based on visualMap-piecewise.pieces. Discrete data (categorical data): categories are defined in visualMap-piecewise.categories. To use segmented visual map, you need to set type to 'piecewise' and choose one of the above three configuration items.

---

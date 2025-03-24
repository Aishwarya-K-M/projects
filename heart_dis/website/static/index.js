const data = {
    labels: [
      'Red',
      'Blue'
    ],
    datasets: [{
      label: 'My First Dataset',
      data: [11, 14],
      backgroundColor: [
        'rgb(255, 99, 132)',
        'rgb(54, 162, 235)'
      ]
    }]
  };

  const config = {
    type: 'polarArea',
    data: data,
    options: {}
  };
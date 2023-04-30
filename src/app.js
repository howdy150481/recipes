import $ from 'jquery';
import 'bootstrap';

import { greet } from './js/scripts.js';
const message = greet('World');
console.log(message);
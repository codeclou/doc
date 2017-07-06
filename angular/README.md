# Angular Styleguide

## Preconditions

 * We use IntelliJ
 * We use Editorconfig (2 space tabs, linux line endings)
 * We use TypeScript
 * We use Tslint
 * We use Angular CLI and the tslint config from there

## General Rules

 * Single Quotes
 * Spacing between curly braces
 * dangling comma (for better git diffs)


:red_circle: BAD

```typescript
import {Foo} from "foo";
```

:white_check_mark: GOOD

```typescript
import { Foo } from 'foo';
```

:red_circle: BAD

```typescript
const foo = {
  bar: 'x',
  foo: 'y'
};
```

:white_check_mark: GOOD (dangling comma)

```typescript
const foo = {
  bar: 'x',
  foo: 'y',
};
```


:red_circle: BAD

```html
<my-comp [foo]="bar" class="foo">content</my-comp>
```

:white_check_mark: GOOD

```typescript
<my-comp
  [foo]="bar"
  class="foo"
>
  content
</my-comp>
```

## IntelliJ

Configure IntelliJ this way:

![](https://codeclou.github.io/doc/intellij/intellij-codestyle-quotes.png)

![](https://codeclou.github.io/doc/intellij/intellij-codestyle-spaces.png)

